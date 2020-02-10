"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”



示例:

输入: citations = [3,0,6,1,5]
输出: 3
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 思路一，先进行排序，再进行比较
    def hIndex(self, citations: [int]) -> int:
        citations.sort(reverse=True)
        for idx, citation in enumerate(citations):
            if idx >= citation:
                return idx
            else:
                break
        return len(citations)

    # 思路二，进行桶排序
    def hIndex2(self, citations):
        n = len(citations)
        buckets = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                buckets[n] += 1
            else:
                buckets[citation] += 1
        cur = 0
        for i in range(n, -1, -1):
            cur += buckets[i]
            if cur >= i:
                return cur
