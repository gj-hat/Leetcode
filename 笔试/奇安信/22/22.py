"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/25 18:50
 @description：
 @modified By：
 @version:     1.0
"""

class Solution:
    def question(self, nums):
        """
        动态规划
        dp数组长度等于原来数组长度 dp[0]=nums[0]
        遍历原来数组
            dp的上一个元素+原数组的当前值 如果(dp上一个元素+原数组)比较小 则说明原数组当前值处重新开始  反正亦然
        :param nums:
        :return:
        """
        nu_li = len(nums)
        dp = [0 for _ in range(nu_li)]
        dp[0] = nums[0]
        for i in range(1, nu_li):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)






if __name__ == '__main__':
    pass