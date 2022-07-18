"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 42. 连续子数组的最大和
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划
        dp数组长度等于原来数组长度 dp[0]=nums[0]
        遍历原来数组
            dp的上一个元素+原数组的当前值 如果(dp上一个元素+原数组)比较小 则说明原数组当前值处重新开始  反正亦然
        :param nums:
        :return:
        """
        nu_li = len(nums)
        if nu_li == 0:
            return 0
        if nu_li == 1:
            return nums[0]
        # 动态规划数组
        dp = [0 for _ in range(nu_li)]

        dp[0] = nums[0]

        # 遍历原数组
        for i in range(1, nu_li):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    nums = [1, 2, -1, 3, 4]

    re = Solution().maxSubArray(nums)
    print(re)
