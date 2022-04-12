import time
from plistlib import Dict



def func(s: dict(type=str, help="this is a string")) -> Dict:
    print(func.__annotations__)
    resList = {}
    length = len(s)
    for i in range(length):
        for j in range(i, length):
            if s[i:j:1] == s[j:i:-1]:
                resList.update({j - i + 1: s[i:j + 1:1]})
            else:
                continue

    return resList


if __name__ == '__main__':
    start = time.clock()
    print(func("dccaccd"))
    stop = time.clock()
    print(stop - start)
