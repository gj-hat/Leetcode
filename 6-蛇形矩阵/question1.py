import string
import time
import math


def func(s: dict(type=str), row: dict(type=int, help="number of row", int=4)) -> string:
    rows = ['' for _ in range(row)]
    direction = True
    rowNum = 0
    resStr = ''
    for j in s:
        rows[rowNum] += j
        if direction:
            rowNum += 1
        else:
            rowNum -= 1
        # Determine if you need to turn
        if rowNum == (row - 1):
            direction = False
        elif rowNum == 0:
            direction = True
    for i in range(row):
        resStr += rows[i]

    return resStr


if __name__ == '__main__':
    start = time.clock()
    st = "PINALSIGYAHRPI"
    row = 4
    print(func(st, row))
    stop = time.clock()
    print(stop - start)
