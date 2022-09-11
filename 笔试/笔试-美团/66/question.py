"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 10:22
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, n1, n2, n3, n4, n5):
        res = []

        site = self.get_all_point(n1)

        for i in site:
            if (abs(n2[0] - i[0]) + abs(n2[1] - i[1]) == n5[0]) and (
                    abs(n3[0] - i[0]) + abs(n3[1] - i[1]) == n5[1]) and (
                    abs(n4[0] - i[0]) + abs(n4[1] - i[1]) == n5[2]):
                res.append(i[0])
                res.append(i[1])
        return res

    def get_all_point(self, n):
        res = []
        for i in range(n):
            for j in range(n):
                res.append([i, j])


if __name__ == '__main__':
    # 输入数字n
    n1 = int(input())

    n2 = input().split()
    n2 = [int(i) for i in n2]
    n3 = input().split()
    n3 = [int(i) for i in n3]
    n4 = input().split()
    n4 = [int(i) for i in n4]

    n5 = input().split()
    n5 = [int(i) for i in n5]
    a = Solution().question(n1, n2, n3, n4, n5)
    print(a[0], "", a[1])
