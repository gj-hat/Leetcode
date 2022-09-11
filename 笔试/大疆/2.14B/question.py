"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/14 19:28
 @description：
 @modified By：
 @version:     1.0
"""
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

class Solution:
    def containsNearbyDuplic(self, nums, k):
        """

        :param nums:   数组
        :param k:    差值K
        :return:
        """
        nu_dic = dict()

        for i in range(len(nums)):
            if not (nums[i] in nu_dic):       # 当key不存在  添加
                nu_dic[nums[i]] = i
            else:  # key存在  判断差值
                if (i - nu_dic[nums[i]]) <= k:
                    return True

        return False

nums_cnt = int(input())
nums = list(map(int, input().split()))

k = int(input())

s = Solution()
res = s.containsNearbyDuplic(nums, k)

print(str(int(res)) + "\n")


if __name__ == '__main__':
    # 输入一个字符串 以空格隔开
    nums = list(map(int, input().split()))
    k = int(input())
    s = Solution()
    res = s.containsNearbyDuplic(nums, k)
    print(str(int(res)) + "\n")



