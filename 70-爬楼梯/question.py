"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 10:08
 @description： 爬楼梯
 @version:     1.0
"""
import time

"""
https://www.bilibili.com/video/BV1eg411w7gn?p=5
数学公式:
f(n) =    1     n = 1
          2     n = 2
          f(n-1) + f(n-2)  n > 2
"""


def algorithm_algorithm(n: int) -> int:
    """
    recursion     递归实现   缺点 会重复计算 时间复杂度很高
    :param n:
    :return:
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return algorithm_algorithm(n - 1) + algorithm_algorithm(n - 2)


def algorithm_algorithm_2(n: int) -> int:
    """
    recursion     递归实现 + hashmap  每次计算前先在hashmap中寻找之前是否已经计算过
    :param n:
    :return:
    """
    res_all = dict()
    if n == 1:
        return 1
    elif n == 2:
        return 2
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
    pre = 2
    pre_pre = 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n+1):
            res = pre + pre_pre
            pre_pre = pre
            pre = res
        return res


if __name__ == '__main__':
    num = input("有多少楼梯:")
    start = time.time()
    print(algorithm_algorithm(int(num)), end=" ")
    stop = time.time()
    print(f"用时:", str(stop - start))

    start = time.time()
    print(algorithm_algorithm_2(int(num)), end=" ")
    stop = time.time()
    print(f"用时:", stop - start)

    start = time.time()
    print(algorithm_ordinary(int(num)), end=" ")
    stop = time.time()
    print(f"用时:", stop - start)


