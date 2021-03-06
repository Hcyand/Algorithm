"""
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]


进阶：是否能在 O(n2) 的时间复杂度内解决？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSumSmaller(self, nums: [int], target: int) -> int:
        # 先对数组进行排序，再利用双指针
        if len(nums) < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target - nums[i]:
                    ans += right - left
                    left += 1
                else:
                    right -= 1
        return ans
