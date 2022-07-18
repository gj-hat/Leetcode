"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 03. 数组中重复的数字
 @modified By：
 @version:     1.0
"""
from typing import List

import numpy


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        初始值等于第一行最右侧元素
        小于: 往下移动一行
        大于: 往左移动一个
        就这样?  对就这样
        :param matrix:
        :param target:
        :return:
        """
        if numpy.size(matrix) == 0:
            return False
        row = len(matrix) - 1
        columns = len(matrix[0]) - 1
        # 行
        i = 0
        # 列
        j = columns

        # 进入循环条件
        while j >= 0 and i <= row:
            # 当前值大于目标值
            if matrix[i][j] > target:
                j -= 1
            # 当前值小于目标值
            elif matrix[i][j] < target:
                i += 1
            # 等于目标值
            else:
                return True
        return False


if __name__ == '__main__':
    # matrix = [
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    matrix = [
        [5, 6, 10, 14],

    ]

    re = Solution().findNumberIn2DArray(matrix, 3)
    print(re)
