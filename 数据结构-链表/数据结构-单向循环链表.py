
"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/15 22:23
 @description： 单向循环列表   加入了尾节点属性 其实可以不用 复杂度差不多 下次别这么干了 出力不讨好
 @modified By：
 @version:     1.0
"""


class Node:
    """ 尾节点的next指向头节点  """
    def __init__(self, ele):
        self.ele = ele
        """" 类似于js  给self中添加next属性 初始值是none  """
        self.next = None


class SingleLinkList:
    def __init__(self, node: Node = None):
        """" 构造函数  可以直接传入一个成型的 链表头节点  下挂线的属性是内部属性
        :type node: Node
        """
        self.__head = node
        if node is not None:
            current = self.__head
            while current.next is not self.__head:
                current = current.next
            self.__tail = current
        else:
            self.__tail = None

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
        if self.is_empty():
            return 0
        else:
            count = 1
            while current is not self.__tail:
                current = current.next
                count += 1
            return count

    def travel(self):
        """
        遍历
        """
        current = self.__head
        if self.length() == 1:
            print(current.ele)
        else:
            while current is not self.__tail:
                print(current.ele, end=" ")
                current = current.next
            print(current.ele)

    def add(self, item):
        """
        头部插入
        :param item: 元素值
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
            self.__tail = node
            node.next = self.__head
        else:
            node.next = self.__head
            self.__head = node

    def append(self, item):
        """
        尾部插入
        :param item:  元素
        """
        node = Node(item)
        if self.is_empty():
            self.add(item)
        else:
            self.__tail.next = node
            node.next = self.__head
            self.__tail = node

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
        if item == self.__head.ele:  # 头节点
            self.__head = current.next
            self.__tail.next = self.__head
        else:
            current = current.next
            while current is not self.__head:
                if current.ele == item:
                    if item == self.__tail.ele:    # 尾节点
                        pre.next = self.__head
                        self.__tail = pre
                    else:
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
            if current.ele == item:
                return index
            current = current.next
            index += 1
        return -1


if __name__ == "__main__":
    test_link = SingleLinkList()
    # print(test_link.is_empty())
    test_link.append(3)
    test_link.append(4)
    test_link.append(5)
    test_link.append(6)
    test_link.append(7)
    # test_link.add(8)
    test_link.travel()

    print(test_link.length())
    # test_link.insert(2, 100)
    # print(test_link.remove(7))
    print(test_link.search(7))

    test_link.travel()
