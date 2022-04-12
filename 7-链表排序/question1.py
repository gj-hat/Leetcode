import time


class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class OperationList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):  # 判断是否为空
        return self.head is None

    def appendNode(self, dataOrNode):  # 尾插
        # item = None
        # 判断是数据还是节点
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        # 如果链表为空 则创建一个链表
        if self.isEmpty():
            self.head = item
            self.length += 1
        else:  # 链表不为空 遍历
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = item
            self.length += 1

    def addIndex(self, dataOrNode, index):  # 指定位置插入
        # item = None
        current = self.head
        # 判断是数据还是节点
        if isinstance(dataOrNode, Node):  # 是节点
            item = dataOrNode
        else:  # 是数值
            item = Node(dataOrNode)
        if self.isEmpty() or index >= self.length:  # 链表为空或者index大于长度则尾插
            self.appendNode(item)
        else:
            if index == 0:  # 插入头节点时
                item.next = current
                self.head = item
                self.length += 1
            else:  # 指定位置
                for i in range(index):
                    current = current.next
                item.next = current.next
                current.next = item

    def delNode(self, value):  # 删除数据
        current = self.head
        node = self.head
        while current is not None:
            current = node.next  # 记录需要删除节点的上一个节点
            if current.data == value:
                node.next = current.next
            current = current.next
            node = node.next

    def updateNode(self, value: help("value"), index: help("this is a index")):  # 修改指定index的数据
        current = self.head
        for i in range(index):
            current = current.next
        current.data = value

    def findIndex(self, value):  # 查询指定元素的下标
        current = self.head
        sum = 0
        while current is not None:
            if current.data == value:
                print("查询的数据节点下标是:%d" % sum)
                break
            sum += 1
            current = current.next
        if sum == 0:
            print("没查到")

    def sortList(self, reverse=False):  # 排序   遍历放入数组  排序数组  再放回去
        current = self.head
        arrTemp = list()
        while current is not None:
            arrTemp.append(current.data)
            current = current.next
        arrTemp.sort(reverse=reverse)
        current = self.head
        for i in arrTemp:
            current.data = i
            current = current.next
        # current = self.head
        # current1 = self.head
        # for i in range(self.length):
        #     for j in range(i+1, self.length):
        #         nodeTemp1 = current
        #         nodeTemp2 = current.next
        #         # if reverse and nodeTemp1.data > nodeTemp2.data:
        #         #     nodeTemp1.data, nodeTemp2.data = nodeTemp2.data, nodeTemp1.data
        #         # elif reverse is False and nodeTemp1.data < nodeTemp2.data:
        #         #     nodeTemp2.data, nodeTemp1.data = nodeTemp1.data, nodeTemp2.data
        #         if nodeTemp1.data < nodeTemp2.data:
        #             nodeTemp2.data, nodeTemp1.data = nodeTemp1.data, nodeTemp2.data
        #         current = current.next
        #     current1 = current1.next
        #     current = current1

    def show(self):  # 遍历显示
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


def func(len1: int, arr1: list, len2: int, arr2: list):
    resList = OperationList()
    for i in arr1:
        resList.appendNode(i)



    for i in arr2:
        resList.appendNode(i)

    # resList.addIndex(9, 1)
    # resList.delNode(3)
    # resList.updateNode(19, 2)
    # resList.findIndex(9)
    resList.sortList(reverse=True)

    resList.show()


if __name__ == '__main__':
    start = time.clock()

    sum1 = input("sum1 length:")
    arrStr = input("")
    arr1 = [int(n) for n in arrStr.split()]

    sum2 = input("sum2 length:")
    arrStr = input("")
    arr2 = [int(n) for n in arrStr.split()]

    print(func(int(sum1), arr1, int(sum2), arr2))

    stop = time.clock()
    print(stop - start)
