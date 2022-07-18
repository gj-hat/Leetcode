"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 12:24
 @description： 合并两个有序数组
 @modified By：
 @version:     1.0
"""


def merge_list(nums1: list, m, nums2: list, n):
    """
    双指针 遍历两个数组 排序好 放入新数组 然后将新数组赋值给nums1
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    temp = list()
    index1 = 0
    index2 = 0
    while index1 < m and index2 < n:
        if nums1[index1] <= nums2[index2]:
            temp.append(nums1[index1])
            index1 += 1
        else:
            temp.append(nums2[index2])
            index2 += 1
    if index1 < m:
        temp += nums1[index1:m]
    elif index2 < n:
        temp += nums2[index2:n]
    for i in range(len(temp)):
        nums1[i] = temp[i]





if __name__ == '__main__':
    nums1 = [0]
    nums2 = [1]
    merge_list(nums1, 1, nums2, 1)
    print(nums1)
