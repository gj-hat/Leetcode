"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 30. 包含min函数的栈
 @modified By：
 @version:     1.0
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return  self.stack[-1]


    def min(self) -> int:
        return min(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

if __name__ == '__main__':

    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.min())
    minStack.pop()
    print(minStack.top())
    print(minStack.min())

