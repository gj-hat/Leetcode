"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/15 09:25
 @description：移除元素
 @modified By：
 @version:     1.0
"""


class Solution:
    def removeElement(self, nums: list, val):
        index = 0
        while  (index < len(nums)):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    a = Solution().removeElement(nums, val)
    print(a)
