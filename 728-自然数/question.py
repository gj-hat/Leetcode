"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   自然数
 @modified By：
 @version:     1.0
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        res = []
        for i in range(left, right + 1):
            li = self.getNumList(i)
            status = 0
            for j in li:
                if (j == 0) or (i % j) != 0:
                    status = 1
                    break
            if status == 0:
                res.append(i)
        return res

    def getNumList(self, num):
        res = []
        while num:
            res.append(num % 10)
            num = num // 10
        res.reverse()
        return res


if __name__ == '__main__':
    test = Solution()

    nums = [100, 200]

    print(test.selfDividingNumbers(nums[0], nums[1]))
