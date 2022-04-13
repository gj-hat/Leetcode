"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/13 12:34
 @description：  删除有序数组中重复项
 @modified By：
 @version:     1.0
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        if nums == []:
            return 0

        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1,1,2]
    a = Solution().removeDuplicates(nums)
