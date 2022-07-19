"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 52. 两个链表的第一个公共节点
 @modified By：
 @version:     1.0
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        temp_dict = dict()
        current = headA
        while current is not None:
            temp_dict[current] = 1
            current = current.next

        current = headB
        while current is not None:
            if temp_dict.get(current) is not None:
                return current
            current = current.next
        return None






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

    re = Solution().getIntersectionNode(head1)
    print(re)
