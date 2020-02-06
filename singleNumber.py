"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]

注意：


结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 常见方法利用哈希表进行求解
# python中也存在counter函数求解
# 本题用按位计算最为方便简洁
class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        acc = 0
        # 按位异或，存在两个相同异或则保持原值
        # 异或0还是原值
        # 同理，二进制两个相同异或保持不变，十进制为十个相同值保持不变
        for i in nums:
            acc ^= i
        n = len(bin(acc)) - 3  # bin()函数计算二进制表达，-3求出两数字不同的最高位
        a, b = 0, 0
        for i in nums:
            if i >> n & 1:
                a ^= i
            else:
                b ^= i
        return b, a
