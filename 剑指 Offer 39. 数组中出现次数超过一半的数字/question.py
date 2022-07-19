"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 39. 数组中出现次数超过一半的数字
 @modified By：
 @version:     1.0
"""

from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        li_dict = dict()
        le = len(nums)
        for i in nums:
            if li_dict.get(i) is not None:
                li_dict[i] += 1
            else:
                li_dict[i] = 1
        for key, value in li_dict.items():
            if value >= math.ceil(le / 2):
                return key


if __name__ == '__main__':
    s = [6, 5, 5]
    re = Solution().majorityElement(s)
    print(re)
