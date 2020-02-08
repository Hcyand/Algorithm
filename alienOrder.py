"""
现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。
假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，
所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。
您需要根据这个输入的列表，还原出此语言中已知的字母顺序。
示例 1：
输入:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
输出: "wertf"
示例 2：
输入:
[
  "z",
  "x"
]
输出: "zx"
示例 3：
输入:
[
  "z",
  "x",
  "z"
]
输出: ""
解释: 此顺序是非法的，因此返回 ""。
注意：
你可以默认输入的全部都是小写字母
假如，a 的字母排列顺序优先于 b，那么在给定的词典当中 a 定先出现在 b 前面
若给定的顺序是不合法的，则返回空字符串即可
若存在多种可能的合法字母顺序，请返回其中任意一种顺序即可
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 需要自己解决问题
import collections
import itertools


class Solution:
    def alienOrder(self, words: [str]) -> str:
        alphabet, not_compared = collections.defaultdict(list), [True] * (len(words) - 1)
        for column in itertools.zip_longest(*words):
            for i in range(len(words) - 1):
                if column[i] is None or column[i + 1] is None:
                    not_compared[i] = False
                if column[i] is not None and (column[i + 1] is None or not not_compared[i]):
                    alphabet[column[i]]
                if not_compared[i] and column[i] != column[i + 1]:
                    alphabet[column[i]].append(column[i + 1])
                    not_compared[i] = False
            if column[-1] is not None:
                alphabet[column[-1]]
        # pprint(alphabet)
        no_parent, res = alphabet.keys() - set(itertools.chain.from_iterable(alphabet.values())), ''
        while no_parent:
            for k in no_parent:
                res += k
                alphabet.pop(k)
            no_parent = alphabet.keys() - set(itertools.chain.from_iterable(alphabet.values()))
        # print(alphabet)
        if alphabet:
            return ''
        return res
