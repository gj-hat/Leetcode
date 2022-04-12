import time


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class NodeFunc(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.next = None

    def createNodeList(self, data=None):
        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            self.head.next = None
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            self.size += 1

    def showNodeList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
        print("size=", self.size)
        print()


def func(nodeList: NodeFunc, n: int):
    length = nodeList.size - n
    current = nodeList.head
    temp = nodeList.head
    i = 0
    while True:
        current = current.next
        i += 1
        if i == length:
            break
        temp = temp.next
    temp.next = current.next
    nodeList.size -= 1


if __name__ == '__main__':
    start = time.clock()
    nums = [-1, 0, 1, 2, -1, -4]
    headNode = NodeFunc()
    for i in nums:
        headNode.createNodeList(i)
    func(nodeList=headNode, n=4)
    headNode.showNodeList()
    stop = time.clock()
    print(f"用时:", stop - start)
