"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3


示例 2:

输入: [3,4,-1,1]
输出: 2


示例 3:

输入: [7,8,9,11,12]
输出: 1


说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


# 桶排序
# 时间为O(n),空间为O(1)
# 分析排序以及缺失数字一定在len(nums)之内
# 索引作为哈希表，边界值挺多的
class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        s = len(nums)
        if s == 0:
            return 1
        for i in range(s):
            while (nums[i] > 0) and (nums[i] <= s):
                if nums[nums[i] - 1] == nums[i]:
                    break
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(s):
            if nums[i] != i + 1:
                return i + 1
        return s + 1


class TestFirstMissingPositive(unittest.TestCase):
    def test_init(self):
        d = Solution()
        self.assertEqual(d.firstMissingPositive([1, 2, 0]), 3)
        self.assertEqual(d.firstMissingPositive([3, 4, -1, 1]), 2)
        self.assertEqual(d.firstMissingPositive([7, 8, 9, 10, 11]), 1)
