"""
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：
-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。
示例：
给定二维网格：
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/walls-and-gates
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def wallsAndGates(self, rooms: [[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def dfs(i, j, steps):
            if i < 0 or i >= row or j < 0 or j >= col or rooms[i][j] < steps:
                return
            rooms[i][j] = min(rooms[i][j], steps)
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                dfs(i + x, j + y, steps + 1)

        if len(rooms) == 0:
            return []
        row = len(rooms)
        col = len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        return rooms
