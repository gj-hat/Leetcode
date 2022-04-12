"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   找到所有数组中消失的数字
 @modified By：
 @version:     1.0
"""


def find_disappeared_numbers(nums):
    res = []
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * (-1)
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    return res


def find_disappeared_numbers_2(nums):
    a = [i for i in range(1, len(nums) + 1)]
    for i in nums:
        for j in a:
            if i == j:
                a.remove(i)
    return a


if __name__ == '__main__':
    nums = [1, 1]

    print(find_disappeared_numbers(nums))
