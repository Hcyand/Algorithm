"""
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。

示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        if not nums:
            return []
        i = 0
        n = len(nums)
        res = []
        while i < n:
            start = i
            while i < n - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == i:
                res.append(str(nums[i]))
            else:
                res.append("{}->{}".format(nums[start], nums[i]))
            i += 1
        return res