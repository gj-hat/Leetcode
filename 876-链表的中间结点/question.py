
"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/29 09:24
 @description： 链表的倒数第k个元素
 @modified By： https://www.bilibili.com/video/BV1eg411w7gn?p=19
 @version:     1.0
"""
import link_list



class Solution:
    """
    方法一:  hash表<index, node>   遍历一次获得长度  然后 hash.get(len - k + 1)
    方法二:  遍历一次 获得长度     再遍历到 len - k + 1
    方法三:  双指针   一个指针的起点为 k-1    另一个从0开始   第一个指针指向None时候 结束

    """

    def getKthFromEnd(self, head, k: int):
        fast_point = head
        low_point = head
        for _ in range(k):
            fast_point = fast_point.next
        while fast_point is not None:
            fast_point = fast_point.next
            low_point = low_point.next
        return low_point

    def getKthFromEnd1(self, head, k: int):
        cur = head
        hash_dic = dict()
        count = 0
        while cur is not None:
            hash_dic[count] = cur
            cur = cur.next
            count += 1
        return hash_dic.get(count-k)


    def getKthFromEnd2(self, head, k: int):
        cur = head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        cur = head
        for _ in range(count - k):
            cur = cur.next
        return cur


# class Solution:
#     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
#         node, n = head, 0
#         while node:
#             node = node.next
#             n += 1
#
#         node = head
#         for _ in range(n - k):
#             node = node.next
#
#         return node


if __name__ == '__main__':
    node = link_list.Node()
    link_list = link_list.SingleLinkList(node)
    link_list.append(1)
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)
    link_list.append(6)
    link_list.append(7)
    link_list.append(8)
    link_list.append(9)

    test = Solution()
    a = test.getKthFromEnd2(node.next, 3)
    print(a.data)
