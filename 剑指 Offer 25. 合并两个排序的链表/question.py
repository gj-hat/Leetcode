"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 25. 合并两个排序的链表
 @modified By：
 @version:     1.0
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2
        reHead = ListNode(0)
        current_re = reHead
        while current_l1 is not None and current_l2 is not None:
            if current_l1.val > current_l2.val:
                current_re.next = current_l2
                current_re = current_re.next
                current_l2 = current_l2.next
            else:
                current_re.next = current_l1
                current_re = current_re.next
                current_l1 = current_l1.next
        if current_l1 is None:
            current_re.next = current_l2
        elif current_l2 is None:
            current_re.next = current_l1
        return reHead.next


if __name__ == '__main__':
    head1 = ListNode(1)
    current = head1
    current.next = ListNode(2)
    current = current.next
    current.next = ListNode(4)

    head2 = ListNode(1)
    current = head2
    current.next = ListNode(3)
    current = current.next
    current.next = ListNode(4)
    current = current.next

    re = Solution().mergeTwoLists(head1, head2)
    print(re)
