"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/29 09:24
 @description： 反转链表
 @modified By： https://www.bilibili.com/video/BV1eg411w7gn?p=16
 @version:     1.0
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        """" 类似于js  给self中添加next属性 初始值是none  """
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
            print(current.data, end=" ")
            current = current.next
        print()

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
            if current.data == item:
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
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1


class Solution:
    def reverseList(self, head):
        cur = head
        li = list()
        while cur is not None:
            li.append(cur.data)
            cur = cur.next
        new_head = Node()
        cur_new_head = new_head
        li.reverse()
        for i in li:
            temp = Node(i)
            while cur_new_head.next is not None:
                cur_new_head = cur_new_head.next
            cur_new_head.next = temp
        return new_head.next

    def reverseList1(self, head):
        res = None
        cur = head
        while cur is not None:
            temp_node = cur.next
            cur.next = res
            res = cur
            cur = temp_node
        return res



if __name__ == '__main__':
    node = Node()
    link_list = SingleLinkList(node)
    link_list.append(1)
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)

    test = Solution()
    a = SingleLinkList(test.reverseList1(node.next))
    a.travel()
