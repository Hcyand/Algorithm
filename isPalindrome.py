"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true


示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。


示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。


进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
"""
import unittest


# 整数转字符串解决问题
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        y = s[::-1]
        if s == y:
            return True
        return False


class TestIsPalindrome(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.isPalindrome(121), True)
        self.assertEqual(d.isPalindrome(-121), False)
        self.assertEqual(d.isPalindrome(10), False)
        self.assertEqual(d.isPalindrome(0), True)

# 不将整数转换为字符串，可以采用除法进行比较
# 负数一定不是回文数
