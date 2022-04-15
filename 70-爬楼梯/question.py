"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 10:08
 @description： 爬楼梯
 @version:     1.0
"""

"""
https://www.bilibili.com/video/BV1eg411w7gn?p=5
数学公式:
f(n) =    1     n = 1
          2     n = 2
          f(n-1) + f(n-2)  n > 2
"""

class Solution:
    # 递归解决
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return res

    def algorithm_algorithm_2(self, n: int) -> int:
        """
        recursion     递归实现 + hashmap  每次计算前先在hashmap中寻找之前是否已经计算过
        :param n:
        :return:
        """
        res_all = dict()
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif res_all.get(n) is not None:
            return res_all.get(n)
        else:
            i = self.algorithm_algorithm_2(n - 1) + self.algorithm_algorithm_2(n - 2)
            res_all[n] = i
            return i

    # 非递归
    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = 0
        temp_pre = 2
        temp_pre_pre = 1
        for i in range(3, n + 1):
            res = temp_pre + temp_pre_pre
            temp_pre_pre = temp_pre
            temp_pre = res
        return res


if __name__ == '__main__':

    # a = Solution().climbStairs(4)
    a = Solution().climbStairs1(4)
    print(a)
