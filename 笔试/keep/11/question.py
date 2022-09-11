"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/30 17:52
 @description：
 @modified By：
 @version:     1.0
"""
import math
class Solution:
    def question(self, num):
        len = num
        count = 0
        if num == 0:
            return 1
        for i in range(len, 0, -1):
            if math.log(i, 2).is_integer():
                count += math.ceil(math.log(i, 2)+1)
            else:
                count += math.ceil(math.log(i, 2))
        return count

    def question1(self, num):
        len = num
        count = []
        if num == 0:
            return 1
        for i in range(len, 0, -1):
            if math.log(i, 2).is_integer():
                count.append(math.ceil(math.log(i, 2)+1))
            else:
                count.append(math.ceil(math.log(i, 2)))
        return count

    def question2(self, num):
        len = num
        count = []
        if num == 0:
            return 1
        for i in range(len, 0, -1):
            if math.log(i, 2).is_integer():
                count.append(math.ceil(math.log(i, 2)+1))
            else:
                count.append(math.ceil(math.log(i, 2)))
        return count

    def a(self, n):
        a = []
        # 第一行一个* 第二行四个* 第三行八个* 第四行十六个*
        for i in range(n):
            if i == 0:
                a.append(1)
            else:
                a.append(a[i-1]*4)
        return a









if __name__ == '__main__':
    in1 = int(input())
    a = Solution().a(in1)
    print(a)
    # pass
