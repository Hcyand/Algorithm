"""
给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，比如："abc" -> "bcd"。这样，我们可以持续进行 “移位” 操作，从而生成如下移位序列：

"abc" -> "bcd" -> ... -> "xyz"

给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。

示例：

输入: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
输出:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-shifted-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 哈希表来判断是否为同一分组
import collections


class Solution:
    def groupStrings(self, strings: [str]) -> [[str]]:
        hash_table = collections.defaultdict(list)
        for s in strings:
            key = self.getKey(s)
            hash_table[key].append(s)
        return [val for val in hash_table.values()]

    def getKey(self, s):
        res = ''
        for i in range(1, len(s)):
            # ord--ASCII数值
            gap_str = str((ord(s[i]) - ord(s[i - 1]) + 26) % 26)
            # zfill:返回指定长度的值
            res += gap_str.zfill(2)
        return res
