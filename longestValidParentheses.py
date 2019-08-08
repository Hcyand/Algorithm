"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"


示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mapping = {")": "("}
        stack = []
        n = 0
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] == top_element:
                    n += 1
            else:
                stack.append(char)
        return n


class TestLongestValidParentheses(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.longestValidParentheses("(())()(()))())))"), 6)
        self.assertEqual(d.longestValidParentheses("("), 0)
        self.assertEqual(d.longestValidParentheses(")"), 0)
