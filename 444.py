"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 18:36
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, low, high):
        res = []
        for i in range(low, high + 1):
            if self.is_prime(i):
                temp = i // 10 % 10 + i % 10
                res.append(temp)
        res.sort()
        return res[0] if len(res) > 0 else 0


    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    a = Solution().question(1, 100)
    print(a)
