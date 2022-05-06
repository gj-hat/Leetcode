"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 10:08
 @description： 斐波那契数列
 @version:     1.0
"""
import time

"""
https://www.bilibili.com/video/BV1eg411w7gn?p=6
数学公式:
f(n) =    0     n = 0
          1     n = 1
          f(n-1) + f(n-2)  n > 1
"""


def algorithm_algorithm(n: int) -> int:
    """
    recursion     递归实现   缺点 会重复计算 时间复杂度很高
    :param n:
    :return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return algorithm_algorithm(n - 1) + algorithm_algorithm(n - 2)


def algorithm_algorithm_2(n: int) -> int:
    """
    recursion     递归实现 + hashmap  每次计算前先在hashmap中寻找之前是否已经计算过
    :param n:
    :return:
    """
    res_all = dict()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif res_all.get(n) is not None:
        return res_all.get(n)
    else:
        i = algorithm_algorithm_2(n - 1) + algorithm_algorithm_2(n - 2)
        res_all[n] = i
        return i


def algorithm_ordinary(n: int) -> int:
    """
    非递归的思路  从f1一直加到fn
    :param n:
    :return:
    """
    res = 0
    pre = 1
    pre_pre = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            res = pre + pre_pre
            pre_pre = pre
            pre = res
        return res


def algorithm_ordinary_3(n: int):
    """
    动态规划
    :param n:
    :return:
    """
    if n <= 1:
        return n
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


if __name__ == '__main__':
    # num = input("有多少楼梯:")
    # start = time.time()
    # print(algorithm_algorithm(int(num)), end=" ")
    # stop = time.time()
    # print(f"用时:", str(stop - start))
    # # #
    # start = time.time()
    # print(algorithm_algorithm_2(int(num)), end=" ")
    # stop = time.time()
    # print(f"用时:", stop - start)
    #
    start = time.time()
    print(algorithm_ordinary(8), end=" ")
    stop = time.time()
    print(f"用时:", stop - start)

    start = time.time()
    print(algorithm_ordinary_3(8), end=" ")
    stop = time.time()
    print(f"用时:", stop - start)
