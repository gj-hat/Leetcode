"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 53 - I. 在排序数组中查找数字 I
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == target:
                count += 1
                for j in range(i + 1, len(nums)):
                    if nums[j] == target:
                        count += 1
                    else:
                        break
                return count
        return count



if __name__ == '__main__':
    nums = [5, 5]
    target = 5

    re = Solution().search(nums, target)
    print(re)
