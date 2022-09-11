"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 11:26
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, n1, n2, n3):
        n = n1[0]
        m = n1[1]
        need = sorted(n2, reverse=True)
        have = sorted(n3, reverse=True)
        res = 0

        for i in range(len(need)):
            temp = self.search_fir_big(need[i], have)
            if temp != -1:
                res += temp
            else:
                return -1

        return res

    # 数组从前往后第一个大于n的数，如果没有，则为-1
    def search_fir_big(self, n, arr):
        res = -1
        for i in arr[::-1]:
            if i >= n:
                return i
        return res


if __name__ == '__main__':
    n1 = [int(x) for x in input().split()]
    n2 = [int(x) for x in input().split()]
    n3 = [int(x) for x in input().split()]
    s = Solution().question(n1, n2, n3)
    print(s)
