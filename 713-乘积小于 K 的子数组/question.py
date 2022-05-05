"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   乘积小于 K 的子数组
 @modified By：
 @version:     1.0
"""
import time


class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        #   nums = [10, 5, 2, 6]
        sum_li = []
        for i in range(len(nums)):
            res = nums[i]
            j = i + 1
            if nums[i] < k:
                sum_li.append(res)
            while j < len(nums):
                res = res * nums[j]
                if res < k:
                    sum_li.append(nums[i: j + 1])
                else:
                    break
                j = j + 1
        return len(sum_li)


    # todo 贪心算法还不会
    def numSubarrayProductLessThan(self, nums: list, k: int) -> int:
        ans, left, cur = 0, 0, 1
        for right, num in enumerate(nums):
            cur *= num
            # 当前到右指针的连乘太大，需要一直挪动左指针直到小于k
            while left <= right and cur >= k:
                cur //= nums[left]
                left += 1
            # 在left到right之间的i, nums[i:right+1]的连乘都满足小于k
            ans += right - left + 1
        return ans




if __name__ == '__main__':
    test = Solution()
    nums = [10, 5, 2, 6]

    # time1 = time.time()
    # print(test.numSubarrayProductLessThanK(nums, 100))
    # time2 = time.time()
    # print(time2 - time1)
    #
    # time1 = time.time()
    # print(test.numSubarrayProductLessThan(nums, 100))
    # time2 = time.time()
    # print(time2 - time1)

