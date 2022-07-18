"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   找到所有数组中消失的数字
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    @staticmethod
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    a = Solution.findDisappearedNumbers(nums=nums)
    print(a)
