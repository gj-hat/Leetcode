"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/13 17:12
 @description：  
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, num, nums):
        # num = len(nums)
        if num < 3:
            return 0
        count = 0
        for i in range(0, num):
            for j in range(i + 1, num):
                for k in range(j + 1, num):
                    if nums[j] < 0 and nums[i]+nums[k] > 0:
                        break
                    if nums[k] == (3*nums[j] - nums[i]):
                        count += 1
        return count


if __name__ == '__main__':
    num = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    s = Solution().question(num, nums)
    print(s)
