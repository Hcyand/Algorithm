"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
方法：
1.暴力法：O(n2）
2.二分法：O(nlogn)
3.栈方法：O(n)
栈方法：为每个数字顺序标记下标，将下标压入栈中，当遇到下降的数字时，栈顶弹出，计算面积，
同时再进行比较，小于栈顶继续弹出，大于则压入。最后将栈中依次弹出，进行计算
"""
import unittest


class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                top = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[top])
            stack.append(i)
        return res


class TsetLargestArea(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
