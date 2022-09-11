"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/18 19:16
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:

    def question(self, n):
        n -= 1
        count = 2 * n
        res = self.recur(n - 1, count)

        return res


    def recur(self, n, count):
        if n == 0:
            return count
        count = (2 * n * (n + 1)) + count
        self.recur(n - 1, count)
        return count


if __name__ == '__main__':
    a = Solution()
    aa = a.question(5)
    print(aa)
