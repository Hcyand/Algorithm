"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 先将数组进行排序，方便判断是否为相同数字
# 出现相同的数字就进行剪枝，需要考虑到两个相同和多个相同的情况

class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]  # 用来检查相同项，以及是否使用过
        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0


if __name__ == '__main__':
    d = Solution()
    print(d.permuteUnique([1, 1, 2]))
