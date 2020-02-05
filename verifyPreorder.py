"""
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。

你可以假定该序列中的数都是不相同的。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：

输入: [5,2,6,1,3]
输出: false

示例 2：

输入: [5,2,1,3,6]
输出: true

进阶挑战：

您能否使用恒定的空间复杂度来完成此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def verifyPreorder(self, preorder: [int]) -> bool:
        # 利用栈思想，当需要更换最小值时进行更换
        stack = []
        new_min = float("-inf")
        for i in range(len(preorder)):
            if preorder[i] < new_min:
                return False
            while stack and preorder[i] > stack[-1]:
                new_min = stack.pop()
            stack.append(preorder[i])
        return True


if __name__ == '__main__':
    d = Solution()
    print(d.verifyPreorder([5, 2, 6, 1, 3]))
    print(d.verifyPreorder([5, 2, 1, 3, 6]))
