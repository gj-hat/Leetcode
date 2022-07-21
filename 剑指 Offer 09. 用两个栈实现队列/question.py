"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 09. 用两个栈实现队列
 @modified By：
 @version:     1.0
"""


class CQueue:
    """
    两个栈  :  先进后出
    队列    :  先进先出
    """

    def __init__(self):
        # 两个栈 一个入栈 一个出栈
        self.stack1 = []
        self.stack2 = []

    def transfer_stack(self):
        """
        有元素的栈 转移到 另一个空栈
        :return:
        """
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return self.stack1

        elif not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2
        else:
            return self.stack1

    def appendTail(self, value: int) -> None:
        if self.stack1:
            self.stack1.append(value)
        elif self.stack2:
            self.stack2.append(value)
        elif self.stack1 == [] and self.stack2 == []:
            self.stack1.append(value)

    def deleteHead(self) -> int:
        qu = self.transfer_stack()
        if not qu:
            return -1
        else:
            res = qu.pop()
            self.transfer_stack()
            return res


if __name__ == '__main__':
    re = CQueue()
    # print(re.deleteHead())  # -1
    # print(re.appendTail(12))  #
    # print(re.deleteHead())  # 12
    # print(re.appendTail(10))  #
    # print(re.appendTail(9))  #
    # print(re.deleteHead())  # 10
    # print(re.deleteHead())  # 9
    # print(re.deleteHead())  # -1
    # print(re.appendTail(20))  #
    # print(re.deleteHead())  # 20
    print(re.appendTail(1))  #
    print(re.appendTail(8))  #
    print(re.appendTail(20))  #
    print(re.appendTail(1))  #
    print(re.appendTail(11))  #
    print(re.appendTail(2))  #
    print(re.deleteHead())  # 1
    print(re.deleteHead())  # 8
    print(re.deleteHead())  # 10
    print(re.deleteHead())  # 1
