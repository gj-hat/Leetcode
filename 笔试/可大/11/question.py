"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 14:57
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def seqSum(self, n: int) -> float:
        if n == 1:
            return 0.50
        if n == 0:
            return 0
        # 0 分子 1 分母
        te = [[1, 2]]
        for i in range(1, n):
            te.append([te[i - 1][1], te[i - 1][1] + te[i - 1][0]])

        le = len(te)
        res = 0
        for i in range(le):
            res += (te[i][0] / te[i][1])

        # res四舍五入保留两位有效小数
        return round(res, 2)


if __name__ == '__main__':
    a = Solution().seqSum(335)
    print(a)
    pass
