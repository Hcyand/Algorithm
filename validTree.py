"""
给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。

示例 1：

输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
输出: true

示例 2:

输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
输出: false

注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edges 中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/graph-valid-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 判断是否为树取决于两个条件：1.是否为连通树    2.是否存在环
# 连通树的判断：len（visited）== n
# 是否存在环的判断：1.边和节点的数量关系  2.访问重复的值(点)
class Solution:
    def validTree(self, n: int, edges: [[int]]) -> bool:
        # 如果边数大于顶点数，则必定存在环
        from collections import defaultdict
        graph = defaultdict(list)
        len_edges = len(edges)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()

        def dfs(i):
            nonlocal len_edges  # nonlocal表示嵌套作用域
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    len_edges -= 1
                    dfs(j)
        dfs(0)
        return len(visited) == n and len_edges == 0


if __name__ == '__main__':
    d = Solution()
    print(d.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
