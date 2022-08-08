"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 42. 连续子数组的最大和
 @modified By：
 @version:     1.0
"""
from typing import List

"""
动态规划
dp数组长度等于原来数组长度 dp[0]=nums[0]
遍历原来数组
    dp的上一个元素+原数组的当前值 如果(dp上一个元素+原数组)比较小 则说明原数组当前值处重新开始  反正亦然
:param nums:
:return:
"""


class Solution:
    def ans(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[size - 1]


if __name__ == '__main__':
    # 用户输入一个数组
    nums = [2, 7, 1, 3, 5, 6, 9]

    a = Solution()
    aa = a.ans(nums)
    print(aa)
