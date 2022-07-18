
"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/15 09:25
 @description：最大子数组和    动态规划
 @modified By：
 @version:     1.0

"""

class Solution:
    def maxSubArray(self, nums: list) -> int:
        # 寄存之前最大值
        temp = 0
        # 存储结果
        res = nums[0]
        for num in nums:
            if temp > 0:
                temp += num
            else:
                temp = num
            res = max(res, temp)
        return res

    def maxSubArray_1(self, nums: list) -> int:
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
    # li = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # li = [1, 2, -1, 5, 0, 0, 0]
    li = [-1, 1, 2, -1, 5, -2, 5, -3, -3, -3, 9]
    # li = [1, 3]
    a = Solution().maxSubArray(li)
    b = Solution().maxSubArray_1(li)
    print(a)
    print(b)
