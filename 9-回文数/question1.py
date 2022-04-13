import time


def func1(number: help("This is an integer of type string")) -> bool:
    lenSt = len(number)
    return True if (lenSt % 2 == 0 and number[0:int(lenSt / 2) + 1:1] == number[lenSt - 1:int(lenSt / 2) - 1:-1]) or (
            lenSt % 2 == 1 and number[:int(lenSt / 2):1] == number[lenSt - 1:int(lenSt / 2):-1]) else False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        len_res = len(res)
        if x < 0:
            return False
        if x == 0:
            return True
        if len_res % 2 == 0:
            return res[:len_res // 2] == res[len_res - 1:(len_res // 2) - 1:-1]
        elif len_res % 2 != 0:
            return res[:len_res // 2] == res[len_res - 1: (len_res // 2):-1]


if __name__ == '__main__':
    start = time.time()

    x = 123121
    a = Solution()
    print(a.isPalindrome(x))

    stop = time.time()
    print(stop - start)
