"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/6 14:42
 @description：  链表重拍
 @modified By：
 @version:     1.0
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def main(self, head1):
        list1, list2 = self.splitList(head1)
        list2 = self.reverseList(list2)

        return self.margeList(list1, list2)

    def margeList(self, head1: ListNode, head2: ListNode):

        head1_cur = head1
        head2_cur = head2
        head1_temp = head1
        head2_temp = head2
        temp = 0
        while head2_temp is not None:
            if temp == 0:
                head2_temp = head2_cur.next
                head2_cur.next = head1_cur
                head2_cur = head2_temp
                temp = 1
            if temp == 1:
                head1_temp = head1_cur.next
                head1_cur.next = head2_cur
                head1_cur = head1_temp
                temp = 0
        if head1_temp is not None:
            self.append(head2, head1_temp)

        return head2

    def append(self, head: ListNode, node: ListNode):
        current = head
        while current.next is not None:
            current = current.next
        current.next = node

    def print_list(self, head):
        while head:
            print(head.val, end=' ')
            head = head.next
        print()

    def splitList(self, head):
        if head is None:
            return None, None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    # 原链表反转
    def reverseList(self, head):
        if head is None:
            return None
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    cur.next = ListNode(2)
    cur = cur.next
    cur.next = ListNode(3)
    cur = cur.next
    cur.next = ListNode(4)
    cur = cur.next
    cur.next = ListNode(5)
    cur = cur.next
    cur.next = ListNode(6)
    cur = cur.next
    cur.next = ListNode(7)

    a = Solution()

    res = a.main(head)
    a.print_list(res)




