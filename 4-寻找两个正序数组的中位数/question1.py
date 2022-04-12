import time


def func(num1, num2):
    for i in num2:
        num1.append(i)
    num1.sort()
    if len(num1) % 2:
        return num1[int(len(num1) / 2)]
    else:
        return (num1[int(len(num1) / 2) - 1] + num1[int(len(num1) / 2)]) / 2


if __name__ == '__main__':
    start = time.clock()
    num1 = [2, 4, 7, 9]
    num2 = [1, 6, 8, 9]
    print(func(num1, num2))
    stop = time.clock()
    print(stop - start)
