"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   字符串相加
 @modified By：
 @version:     1.0
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = list(map(int, num1))
        n2 = list(map(int, num2))
        n1_len = len(n1)
        n2_len = len(n2)

        n1.reverse()
        n2.reverse()
        # 长度置为一样
        if n1_len > n2_len:
            for i in range(n1_len - n2_len):
                n2.append(0)
        elif n2_len > n1_len:
            for i in range(n2_len - n1_len):
                n1.append(0)

        res = []

        n1_point, n2_point = 0, 0
        temp = 0
        while n1_point != (n1_len if n1_len > n2_len else n2_len):
            temp = n1[n1_point] + n2[n2_point] + temp
            if temp <= 9:
                res.append(temp)
                temp = 0
            else:
                res.append(temp - 10)
                temp = 1
            n1_point += 1
            n2_point += 1

        if temp != 0:
            res.append(temp)

        st = ""
        for i in res[::-1]:
            st += str(i)
        return st


if __name__ == '__main__':
    a = "321"
    b = "99876"
    aa = Solution()
    bb = aa.addStrings(a, b)
    print(bb)