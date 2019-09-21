"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


class Solution:
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: [[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        if n == 0:
            return False
        if len(word) == 0:
            return True
        marked = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if self._search_word(board, word, 0, i, j, marked, n, m):
                    return True
        return False

    def _search_word(self, board, word, index, start_x, start_y, marked, n, m):
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        if board[start_x][start_y] == word[index]:
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < n and 0 <= new_y < m and not marked[new_x][new_y] and self._search_word(board, word,
                                                                                                        index + 1,
                                                                                                        new_x, new_y,
                                                                                                        marked, n, m):
                    return True
            marked[start_x][start_y] = False
        return False


class TestExist(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED"), True)
        self.assertEqual(d.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "SEE"), True)
        self.assertEqual(d.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCB"), False)
