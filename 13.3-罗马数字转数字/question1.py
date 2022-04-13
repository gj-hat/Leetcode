import time


def toNum(n):
    if n == 'I':
        return 1
    elif n == 'V':
        return 5
    elif n == 'X':
        return 10
    elif n == 'L':
        return 50
    elif n == 'C':
        return 100
    elif n == 'D':
        return 500
    elif n == 'M':
        return 1000


class Solution:
    def romanToInt(self, s: str) -> int:
        res_list = list(map(toNum, s))
        res_list.append(0)
        index = 1
        res = 0
        while index < len(res_list):
            if res_list[index] <= res_list[index - 1]:
                res += res_list[index-1]
                index += 1
            elif res_list[index] > res_list[index - 1] :
                res += (res_list[index] - res_list[index - 1])
                index += 2
        return res




if __name__ == '__main__':
    start = time.time()

    x = "MCMXCIV"
    a = Solution().romanToInt(x)
    print(a)


    stop = time.time()
    print(f"用时:", stop - start)
