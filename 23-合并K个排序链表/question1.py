import time


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class NodeList(object):
    def __init__(self):
        self.head = None
        # self.next = None
        self.size = 0

    def addNode(self, data):
        newNode = Node(data=data)
        current = self.head
        if current is None:
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


def fun():
    arr1 = [1, 5, 3, 6]
    nodeHead1 = NodeList()
    for i in arr1:
        nodeHead1.addNode(i)
    nodeHead1.showList()

    arr2 = [4, 8, 9, 10, 11]
    nodeHead2 = NodeList()
    for i in arr2:
        nodeHead2.addNode(i)
    nodeHead2.showList()

    arr2 = [6, 7, 8]
    nodeHead3 = NodeList()
    for i in arr2:
        nodeHead3.addNode(i)
    nodeHead3.showList()

    nodeArr = [nodeHead1, nodeHead2, nodeHead3]
    arr3 = list()
    newNodeHead = NodeList()
    for i in nodeArr:
        current = i.head
        while current is not None:
            arr3.append(current.data)
            current = current.next

    arr3.sort()
    for i in arr3:
        newNodeHead.addNode(i)

    newNodeHead.showList()
    return


if __name__ == '__main__':
    start = time.clock()
    fun()
    stop = time.clock()
    print(f"用时:", stop - start)
