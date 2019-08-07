"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。



示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。


示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import unittest


# 使用哈希表+滑动窗口+双指针
class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        # Counter用来计数
        from collections import Counter
        # 存在为空返回[]
        if not s or not words:
            return []
        # 所有字母长度相同，得出单个字母长度
        one_word = len(words[0])
        # 计算单词数,单词总长度
        word_num = len(words)
        len_words = one_word * word_num
        # s长度
        n = len(s)
        # s比len_words短都可以得出
        if n < len_words:
            return []
        # 单词计数
        words = Counter(words)
        res = []
        # 滑动窗口
        for i in range(0, one_word):
            # 用来比较单词数量
            cur_cnt = 0
            left = i
            right = i
            # 用来比较某一单词个数
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    # 存在某一单词更多时，返回到第一个出现该单词的地方
                    # 将该位置之前的单词计数删除
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left + one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    # 相同时即输出初始位置left
                    if cur_cnt == word_num:
                        res.append(left)
        return res


class TestFindSubstring(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9])
        self.assertEqual(d.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), [])
        self.assertEqual(d.findSubstring("word", []), [])
        self.assertEqual(d.findSubstring("", ["word"]), [])
        self.assertEqual(d.findSubstring("", []), [])
        self.assertEqual(d.findSubstring("word", ["happy"]), [])
        self.assertEqual(d.findSubstring("word", ["wor", "dd"]), [])
