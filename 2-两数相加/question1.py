class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# init
def initList(arr):
    head = Node(arr[0])
    p = head
    for i in arr[1:]:
        node = Node(i)
        p.next = node
        p = p.next
    return head


if __name__ == '__main__':
    listTemp1 = initList([2, 4, 3])
    listTemp2 = initList([5, 6, 4])
    listTemp3 = []

    temp = 0

    while listTemp2 is not None:
        if (listTemp1.data + listTemp2.data) < 10:
            listTemp3.append(listTemp1.data + listTemp2.data + temp)
            temp = 0
        else:
            listTemp3.append((listTemp1.data + listTemp2.data) % 10)
            temp = 1

        listTemp1 = listTemp1.next
        listTemp2 = listTemp2.next

    print(listTemp3)
