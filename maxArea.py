"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
"""
import unittest


# 双指针判断
class Solution:
    def maxArea(self, height: [int]) -> int:
        if len(height) < 2:
            return False
        n = 0
        m = len(height) - 1
        max_num = 0
        while (n != m):
            x = min(height[m], height[n])
            max_num = max(x * (m - n), max_num)
            if height[n] >= height[m]:
                m -= 1
            else:
                n += 1
        return max_num


class TestMaxArea(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(d.maxArea([2, 2]), 2)
        self.assertEqual(d.maxArea([2]), False)
