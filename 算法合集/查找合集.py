"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/2 09:16
 @description：  查找算法
 @modified By：
 @version:     1.0
"""

import time


# 顺序查找
def sequence_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1


# 二分查找   要求数组有序
def binary_search(arr: list, target: int):
    start_index = 0
    stop_index = len(arr) - 1

    while start_index <= stop_index:
        mid_index = (stop_index + start_index) // 2
        if target > arr[mid_index]:
            start_index = mid_index + 1
        elif target < arr[mid_index]:
            stop_index = mid_index - 1
        else:
            return mid_index
    return -1


# 插值查找  要求数组有序  本质是二分查找  通过公式缩小范围 自适应选择步长 让其更接近所求
def insertion_search(arr: list, target: int):
    pass


# 斐波那契查找   要求数组有序  本质是二分查找 步长为斐波那契数列(随着数字越来越大 前后比例越接近0.618)
def fibonacci_search(arr: list, target: int):
    pass


# 树表查找


# 分块查找


# 哈希查找


if __name__ == '__main__':
    b = [-1, 0, 3, 5, 6,  9, 12]
    # b = [-1, 0, 3, 5, 9, 12]
    # b = [5]
    print(b)
    # res = sequence_search(b, 9)
    res = binary_search(b, 7)
    print(res)
