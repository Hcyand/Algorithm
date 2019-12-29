"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1


示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


class Solution:
    # 深度优先搜索
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[i][j] = "0"
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                    dfs(tmp_i, tmp_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt


class TestNumIslands(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                                       ["0", "0", "0", "0", "0"]]), 1)
        self.assertEqual(d.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "1"],
                                       ["0", "0", "1", "0", "0"]]), 4)