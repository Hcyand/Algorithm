"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        n = len(nums) - 1
        while n > 0 and nums[n] <= nums[n - 1]:
            n -= 1
        a, b = n, len(nums) - 1
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b -= 1
        j = n - 1
        for k in range(n, len(nums)):
            if nums[k] > nums[j]:
                nums[j], nums[k] = nums[k], nums[j]
                break
