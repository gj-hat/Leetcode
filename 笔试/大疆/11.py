"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/7 19:39
 @description：
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
    # [1, 4, 3, 2]
    def ans(self, li: List) :
        if len(li) == 1:
            return li[0]
        dp = [li[0]]
        for i in range(1, len(li)):
            dp.append(max(dp[i-1]+li[i], li[i]))
        return dp[-1]







        # return 0



if __name__ == '__main__':
    li = [1, 4, 3, 2]
    # 用户输入数据逗号分隔转为数组
    nums = input()
    # 将数组转为int类型
    nums = [int(i) for i in nums]
    a = Solution()
    aa = a.ans(li)
    print(aa)
