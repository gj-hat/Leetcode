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


if __name__ == '__main__':
    # li = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # li = [1, 2, -1, 5, 0, 0, 0]
    li = [-1, 1, 2, -1, 5, -2, 5, -3, -3, -3, 9]
    # li = [1, 3]
    a = Solution().maxSubArray(li)
    print(a)
