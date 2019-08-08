"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：


	所有数字（包括 target）都是正整数。
	解集不能包含重复的组合。


示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]


示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


# 回溯算法！
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        if target == 0:
            return [[]]
        elif not candidates or target < min(candidates):
            return []
        res = []
        for i in candidates:
            # 以下过滤器可避免出现排列不同的重复答案且免排序，x>=i和x<=i都行
            for j in self.combinationSum(list(filter(lambda x: x <= i, candidates)), target - i):
                res.append([i] + j)
        return res


class TestCombinationSum(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.combinationSum([2], 2), [[2]])
