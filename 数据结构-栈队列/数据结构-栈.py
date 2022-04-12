"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/16 22:07
 @description：  栈的顺序表方式实现
 @modified By：
 @version:     1.0
"""

"""
1. 数据存储的基础形式是顺序表和链表
2. 栈和队列都可以使用  顺序表或者链表进行实现
3. python中 list和tup 都是顺序表的形式实现
4. 栈 先进后出,后进先出   队列 先进先出
5. 栈:  对于顺序表而言 前面的为栈底  后面的为栈顶   因为顺序表追加元素的时间复杂度比较低
        对于链表而言   前面的是栈顶  后面的为栈底   链表头节点添加元素 时间复杂度低
"""


class Stack:

    def __init__(self):
        self.__list = []

    def is_empty(self):
        """ 判断栈是否为空 """
        return self.__list == []

    def push(self, item):
        """
        压栈
        :param item:  需要进栈的元素
        """
        self.__list.append(item)

    def pop(self):
        """
        栈顶元素 出栈
        """
        self.__list.pop()

    def peek(self):
        """
        :return:  返回栈顶元素
        """
        return None if self.is_empty() else self.__list[-1]

    def size(self):
        """
        :return:  返回栈的元素个数
        """
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
