"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一，使用递归的思想
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        if not head:
            return None
        stop = False
        left, right = head, head

        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            if n == 1:
                return
            right = right.next
            if m > 1:
                left = left.next
            recurseAndReverse(right, m - 1, n - 1)
            if right == left or right.next == left:
                stop = True
            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next

        recurseAndReverse(right, m, n)
        return head

    # 方法2：翻转链表结构
    def reverseBetween2(self, head, m, n):
        if not head:
            return None
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1
        tail, con = cur, prev
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        if con:
            con.next = prev
        else:
            head.next = prev
        tail.next = cur
        return head
