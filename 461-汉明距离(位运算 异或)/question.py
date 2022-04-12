"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/8 11:03
 @description：  汉明距离
 @modified By：
 @version:     1.0
"""
class Solution:
    def hammingDistance(self, x, y):
        res = x ^ y
        return self.cel_one_count(res)


    def cel_one_count(self, n):
        """
        一方面可以将每个数字以二进制的形式显示出来
        另一方面统计1出现的次数
        :param n:
        :return:
        """
        if n == 0:  # 如果n == 0 直接返回空
            return 0

        res = []  # 结果数组
        b = math.log2(n)  # 计算 log2(n) 即就是有多少位
        if b == int(b):  # 如果恰好等于2的整数次方 则直接可以返回 例如8 = 1000
            # res.append(1)
            # for i in range(int(b)):
            #     res.append(0)
            return 1

        a = int(b) + 1  # 向上取整  有多少位
        while a != -1:  # log2(n)的结果依次递减  直到等于0结束   以9为例
            if (n - (2 ** a)) >= 0:  # n - 2^3 > 0
                res.append(1)  # append(1)
                n = n - (2 ** a)  # n = 9-8 =1
            elif (n - (2 ** a)) < 0:
                res.append(0)  # append(0)
            a -= 1

        count = 0
        for i in res:
            if i == 1:
                count += 1
        return count






if __name__ == '__main__':
    a = Solution()
    a.hammingDistance(1,4)