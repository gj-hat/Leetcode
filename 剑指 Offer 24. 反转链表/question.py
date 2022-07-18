"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 24. 反转链表
 @modified By：
 @version:     1.0
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        temp = []
        current = head
        while current is not None:
            temp.append(current.val)
            current = current.next
        temp.reverse()

        head1 = ListNode(temp[0])
        current1 = head1
        for i in temp[1::]:
            current1.next = ListNode(i)
            current1 = current1.next

        return head1




if __name__ == '__main__':
    head1 = ListNode(1)
    current = head1
    # current.next = ListNode(2)
    # current = current.next
    # current.next = ListNode(3)
    # current = current.next
    # current.next = ListNode(4)
    # current = current.next
    # current.next = ListNode(5)
    # current = current.next

    re = Solution().reverseList(head1)
    print(re)
