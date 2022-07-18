import time


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SingleLinkList:
    def __init__(self, node=None):
        """" 构造函数  可以直接传入一个成型的 链表  下挂线的属性是内部属性"""
        self.__head = node

    def is_empty(self):
        """
        :return: 空:Ture   非空:False
        """
        return self.__head is None

    def length(self):
        """
        :return: 返回链表的长度
        """
        current = self.__head
        count = 0
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def travel(self):
        """
        遍历
        """
        current = self.__head
        while current is not None:
            print(current.val, end=" ")
            current = current.next

    def add(self, item):
        """
        头部插入
        :param item: 元素值
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """
        尾部插入
        :param item:  元素
        """
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, index, item):
        """
        指定位置插入
        :param index: 下角标 0开始
        :param item:
        """
        node = Node(item)
        current = self.__head
        count = 0
        if self.length() < index:
            print("下标越界")
        elif index == 0:
            self.add(item)
        elif index == self.length():
            self.append(item)
        else:
            while count != (index - 1):
                current = current.next
                count += 1
            current_next = current.next
            current.next = node
            node.next = current_next

    def remove(self, item):
        """
        删除节点
        :param item:
        :return:
        """
        current = self.__head
        pre = None
        while current is not None:
            if current.val == item:
                pre.next = current.next
                return True
            else:
                pre = current
                current = current.next
        return False

    def search(self, item):
        """
        查找节点是否层存在
        :param item:  查找的元素
        :return: 找到返回下标 找不到返回-1
        """
        current = self.__head
        index = 0
        while current is not None:
            if current.val == item:
                return index
            current = current.next
            index += 1
        return -1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        node = Node()
        node_current = node
        list1_current = list1
        list2_current = list2
        while list1_current is not None and list2_current is not None:
            if list1_current.val < list2_current.val:
                tempNode = Node(list1_current.val)
                node_current.next = tempNode
                node_current = node_current.next
                list1_current = list1_current.next
            else:
                tempNode = Node(list2_current.val)
                node_current.next = tempNode
                node_current = node_current.next
                list2_current = list2_current.next
        if list1_current is None:
            node_current.next = list2_current
        else:
            node_current.next = list1_current
        return node.next


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(1)
    head1 = SingleLinkList(node1)
    head2 = SingleLinkList(node2)
    head1.append(2)
    head1.append(4)
    head2.append(3)
    head2.append(4)
    head3 = Solution().mergeTwoLists(node1, node2)
    SingleLinkList(head3).travel()




    #
    # node1 = Node()
    # head1 = SingleLinkList(node1)
    # node2 = Node()
    # head2 = SingleLinkList(node2)
    # arr1 = [1, 2, 4]
    # for i in arr1:
    #     head1.append(i)
    # arr2 = [1, 3, 4]
    # for i in arr2:
    #     head2.append(i)
    # head1.travel()

    # start = time.time()
    # print("排序后:")
    # func(head1, head2)
    # stop = time.time()
    # print(f"用时:", stop - start)

