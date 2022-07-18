"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        解法1  暴力
        :param nums:
        :return:
        """
        res = []
        for i in nums:
            if i % 2 == 1:
                res.insert(0, i)
            else:
                res.append(i)
        return res

    def exchange1(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums.insert(0, nums[i])
                nums.pop(i+1)
                i -= 1
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    re = Solution().exchange1(nums)
    print(re)
