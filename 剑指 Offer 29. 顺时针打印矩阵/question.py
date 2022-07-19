"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 29. 顺时针打印矩阵
 @modified By：
 @version:     1.0
"""
from typing import List



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        if row <= 0:
            return []
        columns = len(matrix[0])
        res = []
        left, right, up, down = 0, columns - 1, 0, row - 1
        while True:
            # 左 ---> 右
            if left > right:
                break
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break
            # 上 ---> 下
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            # 右 ---> 左
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:
                break
            # 下 ---> 上
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    re = Solution().spiralOrder(matrix)
    print(re)
