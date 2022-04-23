"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/22 23:10
 @description：最小栈
 @modified By：
 @version:     1.0
"""


class MinStack:

    def __init__(self):
        self.__li = []

    def push(self, val: int) -> None:
        self.__li.append(val)

    def pop(self) -> None:
        self.__li.pop()

    def top(self) -> int:
        return self.__li[-1]

    def getMin(self) -> int:
        return sorted(self.__li)[0]

    def p(self):
        print(self.__li)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    a = MinStack()
    a.push(1)
    a.push(7)
    a.push(3)
    a.push(9)
    a.push(2)
    a.push(0)
    a.p()
    a.getMin()
    a.pop()
    a.pop()
    a.p()
    a.getMin()
