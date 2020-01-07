"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。


进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
思路：
nums1=[2, 5, 6, 8, 12, 15]
nums2=[-5, -2, -1, 1, 5, 8]
判断下标差的最小值
如何比较？较为复杂
是否有简单方法？
上述方法就是双指针解法/滑动窗口
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        if not nums:
            return 0
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0


if __name__ == '__main__':
    d = Solution()
    print(d.minSubArrayLen(7, [2, 3, 1, 3, 4, 3]))
