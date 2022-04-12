"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/2 09:16
 @description：  十大排序算法
 @modified By：
 @version:     1.0
"""

import time


# 冒泡排序  只比较相邻元素
def bubble_sort(arr):
    for i in range(len(arr)):  # 单纯控制次数 使得下面控制的下标依次可以减1 即可
        for j in range(len(arr) - i - 1):  # 控制需要比较元素的下标 依次前移
            if arr[j] > arr[j + 1]:  # 相邻两个比较
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                continue


# 选择排序    每一轮比较选出最大(小)的元素 放置最后
def select_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                continue


# 插入排序       自己写的  从前往后插入   每一次插入都需要 insert/pop
def insert_sort(arr: list):
    res = arr
    for j in range(1, len(res)):
        i = 0
        while i < len(res):  # 从首开始 一直到无序的元素 res[i]
            if res[j] <= res[i]:  # 从前往后 第一个小于的元素下标
                res.insert(i, res[j])  # 插入进去
                res.pop(j + 1)  # 移除原来的元素
                break
            i += 1
    print(res)


# 插入排序2    从后往前插入
def insert_sort2(arr: list):
    res = arr
    size = len(res)
    for i in range(1, size):
        while i > 0:
            if res[i] < res[i - 1]:
                res[i - 1], res[i] = res[i], res[i - 1]
            else:
                break
            i -= 1
    print(res)


# 希尔排序
def shell_sort(arr):
    pass




# 归并排序
def merge_sort(arr:list) -> list:
    """
    归并排序 1. 将数组除二递归    2. 每个小数组都是有序的 进行排序    3. 返回的是另外开辟的数组空间
    :param arr:  list
    :return:     list
    """
    size_arr = len(arr)
    # 递归出口
    if size_arr <= 1:
        return arr

    # 切分成无数个小数组
    mid_val = size_arr // 2
    left_arr = merge_sort(arr[0:mid_val])
    right_arr = merge_sort(arr[mid_val:size_arr])

    # 处理每个小数组
    res = []
    left_point, right_point = 0, 0
    while left_point < len(left_arr) and right_point < len(right_arr):
        if left_arr[left_point] < right_arr[right_point]:
            res.append(left_arr[left_point])
            left_point += 1
        else:
            res.append(right_arr[right_point])
            right_point += 1
    # 剩余数组加入到返回值中
    res += left_arr[left_point:]
    res += right_arr[right_point:]
    return res


# 快速排序
def quick_sort(arr, init_first_index=0, init_index_last=None):
    """
    快速排序   1. 以第一个元素为中位数 一次遍历大于他的放左数组 小于的放右数组
               3. 一次遍历  区分出左右两部分
               4. 递归循环   递归出口 小数组的起始下标大于等于结束下标
    :param arr:   完整的数组  不是切分的数组
    :param init_first_index:    需要处理数组的起始下标
    :param init_index_last:     需要处理数组的结束下标
    :return:
    """
    if init_index_last is None:  # 初始化时候结束下标可以为空
        init_index_last = len(arr) - 1

    if init_first_index >= init_index_last:  # 递归出口
        return

    mid_val = arr[init_first_index]
    point_start = init_first_index  # 记录一下初始值
    point_stop = init_index_last  # 记录一下初始值

    while point_start < point_stop:
        while point_start < point_stop and arr[point_stop] >= mid_val:
            point_stop -= 1  # 指针前移
        arr[point_start] = arr[point_stop]  # 遇到匹配的数据了  和前指针互换
        while point_start < point_stop and arr[point_start] < mid_val:
            point_start += 1  # 指针后移
        arr[point_stop] = arr[point_start]  # 遇到匹配的数据了   和后指针互换
    arr[point_start] = mid_val  # 全部遍历结束了  将中间值复制回来
    quick_sort(arr, init_first_index, point_start - 1)  # 左递归
    quick_sort(arr, point_start + 1, init_index_last)  # 右递归


if __name__ == '__main__':
    b = [1, 4, 6, 9, 6, 3, 1, 4, 6, 8, 0, 6, 4, 2]
    # b = [4, 1, 3]
    print(b)
    print(b)


    start = time.time()
    # bubble_sort(b)
    # quick_sort(b)
    mer_arr = merge_sort(b)
    print(mer_arr)
    # print(b)
    stop = time.time()
    print(stop - start)

