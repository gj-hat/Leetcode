"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   链表的中间结点
 @modified By：   https://www.bilibili.com/video/BV1eg411w7gn?p=18
 @version:     1.0
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    另一种方法:  双指针  快指针走2  慢指针走1
            循环条件: 快指针的next不为None就可以
            结束条件:  快指针next.next为None就结束  慢指针的位置就是所求的元素
    """
    def middleNode(self, head):
        res_li = list()
        cur = head
        while cur is not None:
            res_li.append(cur.val)
            cur = cur.next
        len_res_li = len(res_li)
        cen_index = len_res_li//2 + 1
        cur = head
        count = 1
        while cen_index != count:
            count += 1
            cur = cur.next
        return cur








