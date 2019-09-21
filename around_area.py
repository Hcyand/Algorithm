"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X


运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X


解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n < 1:
            return board
        m = len(board[0])
        if n <= 2 or m <= 2:
            return board
        market = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if board[i][0] == 'O':
                self.search_around(board, market, i, 0, n, m)
            if board[i][m - 1] == 'O':
                self.search_around(board, market, i, m - 1, n, m)
        for j in range(m):
            if board[0][j] == 'O':
                self.search_around(board, market, 0, j, n, m)
            if board[n - 1][j] == 'O':
                self.search_around(board, market, n - 1, j, n, m)
        for i in range(n):
            for j in range(m):
                if market[i][j] is True:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def search_around(self, board, market, i, j, n, m):
        if board[i][j] == 'O':
            market[i][j] = True
            for direction in self.directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < n and 0 <= new_j < m and not market[new_i][new_j]:
                    self.search_around(board, market, new_i, new_j, n, m)
