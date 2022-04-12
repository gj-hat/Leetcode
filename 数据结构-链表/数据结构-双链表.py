
"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/15 22:23
 @description： 双向链表
 @modified By：
 @version:     1.0
"""


class Node:
    def __init__(self, ele):
        """ 节点类  包含三个属性 元素值 上一个/下一个地址  """
        self.ele = ele
        self.next = None
        self.previous = None


class DoubleLinkList:
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
        """ 遍历 """
        current = self.__head
        while current is not None:
            print(current.ele, end=" ")
            current = current.next
        print()

    def add(self, item):
        """
        头部插入
        :param item: 元素值
        """
        node = Node(item)    # new一个节点
        node.next = self.__head   # 新节点的next指向原来的头节点
        self.__head = node        # 将新节点设置为链表的头节点
        self.__head.next.previous = self.__head   # 将头节点后的第二节点的prev指向原来头节点
        # node.next.previous = node   # 和上面等价

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
            current.next.previous = current

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
            # 配置新节点
            node.previous = current  # 新节点的上一个等于当前元素
            current.next.previous = node      # 当前元素的下一个节点的上一个等于新节点
            node.next = current.next   # 新节点的下一个等于当前元素的下一个
            # 正式加入新节点
            current.next = node

    def remove(self, item):
        """
        删除节点
        :param item:
        :return:
        """
        current = self.__head
        while current is not None:
            if current.ele == item:
                if current is self.__head:    # 如果删除的是头节点
                    self.__head = current.next
                    if current.next is not None:   # 判断链表是不是只有一个节点
                        current.next.previous = None
                else:
                    current.previous.next = current.next   # 当前的上一个节点的下一个指向当前的下一个节点
                    if current.next is not None:
                        current.next.previous = current.previous  # 当前的下一个节点的上一个指向当前的上一个节点
                return True
            else:
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
    test_link = DoubleLinkList()
    # print(test_link.is_empty())
    test_link.append(3)
    test_link.append(4)
    test_link.append(6)
    test_link.append(7)
    test_link.append(8)
    test_link.insert(2, 100)
    test_link.remove(100)
    # print(test_link.remove(6))
    test_link.travel()
