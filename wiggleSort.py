"""
给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。

示例:

输入: nums = [3,5,2,1,6,4]
输出: 一个可能的解答是 [3,5,1,6,2,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-sort
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def wiggleSort(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        nums.sort()
        tmp = []
        i = 0
        j = len(nums) - 1
        while i <= j:
            tmp.append(nums[i])
            if i < j:
                tmp.append(nums[j])
            i += 1
            j -= 1
        return tmp


if __name__ == '__main__':
    d = Solution()
    print(d.wiggleSort([3, 5, 2, 1, 6, 4]))
