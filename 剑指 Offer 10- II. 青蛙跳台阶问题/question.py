"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 10- II. 青蛙跳台阶问题
 @modified By：
 @version:     1.0
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        pre = 2
        pre_pre = 1
        res = pre + pre_pre
        for i in range(3, n):
            pre_pre = pre
            pre = res
            res = pre + pre_pre
        return res % 1000000007



if __name__ == '__main__':
    re = Solution().fib(7)
    print(re)

