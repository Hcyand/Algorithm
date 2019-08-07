"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.


说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = node = head
        for i in range(n):
            node = node.next
        if not node:
            return head.next
        while node.next:
            cur = cur.next
            node = node.next
        cur.next = cur.next.next
        return head


class TestRemoveNthFromEnd(unittest.TestCase):
    def test_init(self):
        d = Solution()
        list_1 = [5, 4, 3, 2, 1]
        l1 = None
        for i in list_1:
            l1 = ListNode(i, l1)
        list_2 = [5, 3, 2, 1]
        l2 = None
        for i in list_2:
            l2 = ListNode(i, l2)
        # 链表的单元测试？？？？
        self.assertEqual(d.removeNthFromEnd(l1, 2), l2)
