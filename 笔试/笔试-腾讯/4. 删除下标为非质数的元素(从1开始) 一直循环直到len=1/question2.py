"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/24 20:22
 @description：
 @modified By：
 @version:     1.0
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param a int整型一维数组
# @return int整型
#
class Solution:
    def getNumber(self, a: list) -> int:

        while len(a) != 1:
            a_len = len(a)
            temp_li = self.getPrime(a_len)
            for i in temp_li[::-1]:
                a.pop(i-1)
        print(a)
        return a[0]

    # 0到10之间所有质数
    def getPrime(self, n: int) -> list:
        res = []
        for i in range(1, n + 1):
            if not self.isPrime(i):
                res.append(i)
        return res

    def isPrime(self, n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    # a = Solution().getNumber([1,2,3,4])
    a = Solution().getNumber([3,1,1,4,5,6])
    # a = Solution().getPrime(4)
    print(a)
