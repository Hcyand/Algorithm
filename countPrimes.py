"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 厄拉多塞筛法
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i:n:i] = [0] * len(isPrimes[i * i:n:i])

        return sum(isPrimes)


if __name__ == '__main__':
    d = Solution()
    print(d.countPrimes(10))