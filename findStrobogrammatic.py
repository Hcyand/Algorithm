"""
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

找到所有长度为 n 的中心对称数。

示例 :

输入:  n = 2
输出: ["11","69","88","96"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strobogrammatic-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> [str]:
        record = dict()
        record[1] = ["0", "1", "8"]
        record[2] = ["11", "69", "88", "96"]
        pair = ["00", "11", "88", "69", "96"]
        if n <= 2:
            return record[n]
        cnt = 3
        while cnt <= n:
            tmp = []
            if (cnt - 1) % 2 == 0:
                for item in record[cnt - 1]:
                    for num in record[1]:
                        tmp.append(item[:len(item) // 2] + num + item[len(item) // 2:])
            else:
                for item in record[cnt - 2]:
                    for num in pair:
                        tmp.append(item[:len(item) // 2] + num + item[len(item) // 2:])
            record[cnt] = tmp
            cnt += 1
        return record[n]


if __name__ == '__main__':
    d = Solution()
    print(d.findStrobogrammatic(2))
    print(d.findStrobogrammatic(3))
    print(d.findStrobogrammatic(4))
