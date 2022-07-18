"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 10- I. 斐波那契数列
 @modified By：
 @version:     1.0
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        pre = 1
        pre_pre = 0
        res = pre + pre_pre
        for i in range(2, n):
            pre_pre = pre
            pre = res
            res = pre + pre_pre
        return res % 1000000007



if __name__ == '__main__':
    re = Solution().fib(5)
    print(re)

