"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 14:57
 @description：
 @modified By：
 @version:     1.0
"""
import collections
from typing import List


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

    def shortestPath(self, maze: List[List[int]]) -> List[Point]:
        res = []
        temp_path = []
        a = self.get_boundary(maze)
        for i in a:
            x, y = 2, 2
            x_temp, y_temp = i.x, i.y
            while x_temp != x and y_temp != y:
                if maze[x_temp][y_temp] == 1:
                    continue
                if maze[x_temp][y_temp + 1] == 0:  # 右
                    break
                if maze[x_temp][y_temp - 1] == 0:  # 左
                    break
                if maze[x_temp + 1][y_temp] == 0:  # 下
                    break
                if maze[x_temp - 1][y_temp] == 0:  # 上
                    break

        return -1

    # 返回maze入口
    def get_boundary(self, maze):
        boundary = []
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 0 and (i == 0 or j == 0 or j == 3 or i == 3):
                    boundary.append(Point(i, j))
        return boundary


if __name__ == '__main__':
    re = Solution().shortestPath([[0, 1, 1, 1], [0, 0, 0, 1], [1, 0, 8, 1], [1, 0, 1, 1]])
    aa = Solution().uniquePaths(3, 2)
    print(aa)
