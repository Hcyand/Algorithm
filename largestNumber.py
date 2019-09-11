"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210

示例 2:

输入: [3,30,34,5,9]
输出: 9534330

说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest
from functools import cmp_to_key


class Solution(object):
    def strCmp(self, s1, s2):
        if s1 + s2 > s2 + s1:
            return 1
        return -1

    def largestNumber(self, nums):
        s = set(nums)
        if len(s) == 1 and 0 in s:  # 处理[0,0]这种用例
            return "0"
        nums = sorted([str(n) for n in nums], key=cmp_to_key(self.strCmp), reverse=True)
        return "".join(nums)


class TestLargestNumber(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.largestNumber([10, 2]), '210')
