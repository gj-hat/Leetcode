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

    #  贪心算法
    def numSubarrayProductLessThan(self, nums: list, k: int) -> int:
        #     nums = [10, 5, 2, 6]
        count, start, res = 0, 0, 1
        # 枚举遍历数组 key=下标  value=元素
        for stop, num in enumerate(nums):
            # res = res * 当前元素
            res *= num
            # 当res大于k值了 进入while循环
            while start <= stop and res >= k:
                res //= nums[start]
                start += 1
            # 在start到stop之间的i, nums[i:stop+1]的连乘都满足小于k
            count += stop - start + 1
        return count



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

    time1 = time.time()
    print(test.numSubarrayProductLessThan(nums, 100))
    time2 = time.time()
    print(time2 - time1)
