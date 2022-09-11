"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/31 21:12
 @description：
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def question(self, num, arr: List):
        res = [0 for _ in range(num)]
        for i in range(len(arr)):
            res = self.question1([arr[i][0], arr[i][1]], res)

        for i in range(len(res)):
            if res[i] == 0:
                res[i] = 1
            else:
                res[i] = 0
        print(res)
        return res

    # arr1小的  arr2大的
    def question1(self, arr1: List, arr2: List):
        for i in range(arr1[0]-1, arr1[1]):
            arr2[i] = 1
        return arr2


if __name__ == '__main__':

    # in1 = input().split(" ")
    # in1 = [int(i) for i in in1]
    # in2 = []
    # for i in range(in1[1]):
    #     temp = input().split(" ")
    #     in2.append([int(i) for i in temp])
    a = Solution().question(10, [[1, 4, 2], [3, 6, 2], [10, 10, 1]])
    # a = Solution().question(in1[0], in2)
