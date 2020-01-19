"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        if t < 0 or k < 0:
            return False
        all_bucket = {}
        bucket_size = t + 1
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size
            if bucket_num in all_bucket:
                return True
            all_bucket[bucket_num] = nums[i]
            if (bucket_num - 1) in all_bucket and abs(all_bucket[bucket_num - 1] - nums[i]) <= t:
                return True
            if (bucket_num + 1) in all_bucket and abs(all_bucket[bucket_num + 1] - nums[i]) <= t:
                return True
            if i >= k:
                all_bucket.pop(nums[i - k] // bucket_size)
        return False
