"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。


示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 存放字符串和位置的字典
        st = {}
        # 用于标记当前st字符串起始位置
        i = 0
        # 存放最长字符串长度
        ans = 0
        for j in range(len(s)):
            if s[j] in st:
                # 判断重复位置在i前或i后，i取大值
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            # 加入字典s[j]对应j+1
            st[s[j]] = j + 1
        return ans


class TestMaxLenStr(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.lengthOfLongestSubstring('test'), 3)
        self.assertEqual(d.lengthOfLongestSubstring('add'), 2)
        self.assertEqual(d.lengthOfLongestSubstring(''), 0)
