import time


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class NodeList(object):
    def __init__(self):
        self.head = Node()
        # self.head = Node()
        self.size = 0

    def addNode(self, data):
        newNode = Node(data=data)
        current = self.head
        if current.next is None and current.data is None:
            self.head = newNode
        else:
            while current.next is not None:
                current = current.next
            current.next = newNode

    def showList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


def swapPairs(head):
    if head is None or head.next is None:
        return head

    firstNode = head
    secondNode = head.next

    res = swapPairs(secondNode.next)

    firstNode.next = res
    secondNode.next = firstNode

    return secondNode


def fun():
    arr = [1, 2, 3, 4]
    nodeList = NodeList()
    for i in arr:
        nodeList.addNode(i)
    nodeList.showList()

    print()
    a = swapPairs(nodeList.head)
    b = a
    while b is not None:
        print(b.data, end=" ")
        b = b.next

    print()
    nodeList.showList()

    return


if __name__ == '__main__':
    start = time.clock()
    fun()
    stop = time.clock()
    print(f"用时:", stop - start)
