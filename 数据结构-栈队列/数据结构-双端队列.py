"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/16 23:28
 @description：  双端队列
 @modified By：
 @version:     1.0
"""


class Deque:
    def __init__(self):
        self.__list = list()

    def add_front(self, item):
        """
        从队列的前端插入
        :param item:   插入的元素
        """
        self.__list.insert(0, item)

    def add_rear(self, item):
        """
        从队列的后端插入
        :param item:  插入的元素
        """
        self.__list.append(item)

    def remove_front(self):
        """
        从队列的前端移除元素
        """
        self.__list.remove(0)

    def remove_rear(self):
        """
        从队列的后端移除元素
        """
        self.__list.remove(-1)

    def is_empty(self):
        """
        判空
        :return: Boolean
        """
        return self.__list == []

    def size(self):
        """
        :return: 队列的长度
        """
        return len(self.__list)


if __name__ == '__main__':
    s = Deque()

