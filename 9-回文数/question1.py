import time


def func1(number: help("This is an integer of type string")) -> bool:
    lenSt = len(number)
    return True if (lenSt % 2 == 0 and number[0:int(lenSt / 2) + 1:1] == number[lenSt - 1:int(lenSt / 2) - 1:-1]) or (
            lenSt % 2 == 1 and number[:int(lenSt / 2):1] == number[lenSt - 1:int(lenSt / 2):-1]) else False


if __name__ == '__main__':
    start = time.clock()
    num = input("please input a number:")
    print(type(num))
    print(func1(num))

    stop = time.clock()
    print(stop - start)
