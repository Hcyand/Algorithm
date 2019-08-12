"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 方法一可以使用O(n)一次遍历，当出现sum为负数时归0，继续相加，保留最大值，如果全为负数，保留最大负数
# 方法二，使用分治法，时间为O(nlog(n))

# 分治法
# 计算出左边最大和右边最大，最后比较三个数哪个更大即成立
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            max_right = self.maxSubArray(nums[len(nums) // 2:])
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(max_l.max_r, max_l + max_r)
