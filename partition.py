"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 回溯算法
# 动态规划：将是否为回文串进行标记dp[i][j] is True or False
class Solution:
    # 回溯算法
    def partition_1(self, s) -> [[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res

    def partition_2(self, s) -> [[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True

        def helper(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    helper(j + 1, tmp + [s[i:j + 1]])

        helper(0, [])
        return res


if __name__ == '__main__':
    d = Solution()
    print(d.partition_1(s="abb"))
    print(d.partition_2(s="aab"))
