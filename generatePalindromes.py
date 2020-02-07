"""
回文排列II

给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。

如不能形成任何回文排列时，则返回一个空列表。

示例 1：

输入: "aabb"
输出: ["abba", "baab"]

示例 2：

输入: "abc"
输出: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class Solution:
    def generatePalindromes(self, s: str) -> [str]:
        char_count = collections.Counter(s)
        odd_char = ''
        even_char = ''
        for char in char_count:
            if char_count[char] % 2 != 0:
                odd_char += char
                char_count[char] -= 1
            if len(odd_char) > 1:
                return []
            even_char += char * (char_count[char] // 2)

        self.res = []
        visited = [False for _ in range(len(even_char))]
        self.BackTracking(even_char, '', visited, odd_char)
        return self.res

    def BackTracking(self, even_char, sub_string, visited, odd_char):
        if len(sub_string) == len(even_char):
            s = sub_string + odd_char + sub_string[::-1]
            self.res.append(s)
            return

        for i in range(len(even_char)):
            if visited[i]:
                continue
            if i > 0 and even_char[i] == even_char[i - 1] and not visited[i - 1]:
                continue
            sub_string += even_char[i]
            visited[i] = True
            self.BackTracking(even_char, sub_string, visited, odd_char)
            visited[i] = False
            sub_string = sub_string[:-1]


if __name__ == '__main__':
    d = Solution()
    print(d.generatePalindromes('abba'))
