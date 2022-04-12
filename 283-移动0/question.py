"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 12:24
 @description： 合并两个有序数组
 @modified By：
 @version:     1.0
"""


def move_zero(nums):
    size = len(nums)
    j = 0
    for i in range(size):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    # for i in range(size - 1, size - j - 1, -1):
    for i in range(j, size):
        nums[i] = 0


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    move_zero(nums)
    print(nums)
