"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。
所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。
说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
1:示例

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]

示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-itinerary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


# 关键在于一定存在一条路线使得全部遍历，即如何走到了一个死胡同，那么从这个死胡同的终点作为起点进行遍历则可以一次性走完
# 且所走路线正好是完整路线的返向，即返回s[::-1]
# 另外关键在于这种字典路线选择，一般选择回溯法进行判断
class Solution:
    def findItinerary(self, tickets: [[str]]) -> [str]:
        paths = collections.defaultdict(list)
        for start, tar in tickets:
            paths[start].append(tar)
        for start in paths:
            paths[start].sort(reverse=True)
        s = []

        def search(start):
            while paths[start]:
                search(paths[start].pop())
            s.append(start)

        search("JFK")
        return s[::-1]


if __name__ == '__main__':
    d = Solution()
    d.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
