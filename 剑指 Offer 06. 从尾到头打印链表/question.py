"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 06. 从尾到头打印链表
 @modified By：
 @version:     1.0
"""
# Definition for singly-linked list.
from typing import List
import link_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        current = head
        res = []
        while current is not None:
            res.append(current.val)
            current = current.next
        res.reverse()
        return res





if __name__ == '__main__':
    head = ListNode(1)

    link = link_list.SingleLinkList(head)
    link.append(2)
    link.append(3)




    re = Solution().reversePrint(head)
    print(re)




