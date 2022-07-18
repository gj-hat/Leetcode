"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 03. 数组中重复的数字
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        res = dict()
        for i in nums:
            if res.get(i) is None:
                res[i] = 0
            else:
                return i




if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    re = Solution().findRepeatNumber(nums)
    print(re)




