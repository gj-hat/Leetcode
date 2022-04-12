"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/29 16:35
 @description：用栈实现队列
 @modified By：  https://www.bilibili.com/video/BV1eg411w7gn?p=21&spm_id_from=333.851.header_right.history_list.click
 @version:     1.0
"""


class MyQueue:

    def __init__(self):
        self.in_qu = []
        self.out_qu = []

    def in_to_out(self):
        while self.in_qu:
            self.out_qu.append(self.in_qu.pop())


    def out_to_in(self):
        while self.out_qu:
            self.in_qu.append(self.out_qu.pop())

    # 入队列  最后添加元素
    def push(self, x: int) -> None:
        if self.out_qu:
            self.out_to_in()
        self.in_qu.append(x)

    # 出队列  首元素
    def pop(self) -> int:
        if self.in_qu:
            self.in_to_out()
        return self.out_qu.pop()

    # 返回首元素
    def peek(self) -> int:
        if self.in_qu:
            self.in_to_out()
        return self.out_qu[-1]

    def empty(self) -> bool:
        return not bool(self.in_qu) and not bool(self.out_qu)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    test = MyQueue()

    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.pop()
    test.push(5)
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.pop())

    print(test.empty())
