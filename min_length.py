"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 思路，动态规划过程
# 从一点到另一点最短距离，由其上和右的更小值决定
# 因此动态规划出相应的最小值
# 同时不使用额外空间
import unittest


class Solution:
    def minPathSum(self, grid: [[]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[len(grid) - 1][len(grid[0]) - 1]


class TestMinPathSum(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
