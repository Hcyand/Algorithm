"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。


示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        res = ""
        for i in range(n):
            # dp[0][0]=1
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                    dp[i][j] = 1
                if dp[i][j] and i - j + 1 > max_len:
                    max_len = i - j + 1
                    res = s[j:i + 1]
        return res


class TestLongestPalindrome(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.longestPalindrome('djjdjjfff'), 'jjdjj')
        self.assertEqual(d.longestPalindrome('aaa'), 'aaa')
        self.assertEqual(d.longestPalindrome(''), '')
        # 存在问题，aba不能通过，唯一解问题有待解决
        self.assertEqual(d.longestPalindrome('adaba'), 'ada')
