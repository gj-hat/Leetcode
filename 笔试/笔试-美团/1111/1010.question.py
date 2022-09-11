"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/27 16:16
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, arr1, nums):
        arr_yuan = [i for i in range(1, nums + 1)]
        for i in arr1:
            arr_yuan.remove(i)
            arr_yuan.insert(0, i)

        return arr_yuan


if __name__ == '__main__':
    inp2 = input().split(" ")
    arr2 = [int(i) for i in inp2]
    inp = input().split(" ")
    arr1 = [int(i) for i in inp]
    a = Solution().question(arr1, arr2[0])
    for i in a:
        print(i, end=" ")

