"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 17. 打印从1到最大的n位数
 @modified By：
 @version:     1.0
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        current = head
        current = current.next
        pre_current = head
        while current.val != val:
            pre_current = pre_current.next
            current = current.next
        pre_current.next = pre_current.next.next
        return head


if __name__ == '__main__':
    head1 = ListNode(1)
    current = head1
    current.next = ListNode(2)
    current = current.next
    current.next = ListNode(3)
    current = current.next
    current.next = ListNode(4)
    current = current.next
    current.next = ListNode(5)
    current = current.next
    val = 2
    re = Solution().deleteNode(head1, val)
    print(re)
