"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/15 09:25
 @description：搜索插入的位置
 @modified By：
 @version:     1.0
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    # nums = [1, 3]
    val = 5
    a = Solution().searchInsert(nums, val)
    print(a)
