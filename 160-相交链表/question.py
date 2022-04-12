"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/28 17:19
 @description：  相交链表   核心代码(懒得写链表了 )
 @modified By：
 @version:     1.0
"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ 方法一  哈希表  """
    def getIntersectionNode(self, headA, headB) :
        temp = dict()
        curA = headA
        curB = headB
        while curA is not None:
            temp[curA] = 0
            curA = curA.next
        while curB is not None:
            if temp.get(curB) is not None:
                return curB
            curB = curB.next
        return None

    """" 
    方法二  双指针对应两个链表
    1. 同时同速走
    2. 一个等于null了  就交换指针指向的链表  另一个同理
    3. 两个指针相遇就说明有  两个指针都等于null了  说明没有
    """


    """" 
    方法三  双指针对应两个链表
    1. 两个链表的长度相减=n  短的链表从头走   长的链表从n开始走
    2. 两个指针相遇就说明有  两个指针都等于null了  说明没有
    """