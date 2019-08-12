"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 回溯法
# 对于所有的主对角线有 行号 + 列号 = 常数，对于所有的次对角线有 行号 - 列号 = 常数
class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        def backtrack():
            row = len(queens)  # 下标为行的索引
            if row == n:  # 若已经有n个元素满足
                output.append(queens[:])
            for col in range(n):  # 从第一行第一列开始
                if col not in queens and xy_dif[row - col] and xy_sum[row + col]:  # 判断是否可以放棋子
                    queens.append(col)
                    xy_dif[row - col], xy_sum[row + col] = False, False
                    backtrack()  # 向下一行探索
                    queens.pop()  # 回溯，挪开棋子
                    xy_dif[row - col], xy_sum[row + col] = True, True

        queens = []
        xy_dif = [True] * (2 * n - 1)
        xy_sum = [True] * (2 * n - 1)
        output = []  # 所有结果集
        backtrack()
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in output]
