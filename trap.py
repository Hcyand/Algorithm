"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""
import unittest


# 方法：双指针判定列O(n)/判断行时间为O(n*m)
class Solution:
    def trap(self, height: [int]) -> int:
        if not height: return 0
        left = 0
        right = len(height) - 1
        res = 0
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res


class TestTrap(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
