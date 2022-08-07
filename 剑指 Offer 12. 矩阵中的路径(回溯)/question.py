"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 12. 矩阵中的路径(回溯)   回溯算法
 @modified By：
 @version:     1.0
"""
from typing import List

"""
回溯算法 解题步骤: 
1. 判断当前情况是否非法，如果非法就立即返回；
2. 当前情况是否已经满足递归结束条件，如果是就将当前结果保存起来并返回；
3. 当前情况下，遍历所有可能出现的情况并进行下一步的尝试；
4. 递归完毕后，立即回溯，回溯的方法就是取消前一步进行的尝试。
function fn(n) {
    // 第一步：判断输入或者状态是否非法？
    if (input/state is invalid) {
        return;
  }
    // 第二步：判读递归是否应当结束?
    if (match condition) {
        return some value;
  }
    // 遍历所有可能出现的情况
    for (all possible cases) {
        // 第三步: 尝试下一步的可能性
        solution.push(case)
        // 递归
        result = fn(m)
        // 第四步：回溯到上一步
        solution.pop(case)
    }
}
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)

        # 判断是否越界(非回溯必须)
        def crossBorder(x, y):
            return x < 0 or y < 0 or x >= m or y >= n

        # 搜索函数
        def dfs(i, j, index) -> bool:
            # 1. 满足结果 找到了   判断输入还是状态是否非法？
            if board[i][j] == word[index] and index == word_len - 1:
                return True

            # 2. 匹配不上  终止循环
            if board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = -1


            # 3. 继续搜索   遍历所有可能出现的情况
            # 向上搜索
            if (not crossBorder(i-1, j)) and dfs(i-1, j, index+1):
                return True
            # 向下搜索
            if (not crossBorder(i+1, j)) and dfs(i+1, j, index+1):
                return True
            # 向左搜索
            if (not crossBorder(i, j-1)) and dfs(i, j-1, index+1):
                return True
            # 向右搜索
            if (not crossBorder(i, j+1)) and dfs(i, j+1, index+1):
                return True

            board[i][j] = temp

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [["a", "b"], ["c", "d"]]
    word = "abcd"

    re = Solution().exist(board, word)
    print(re)
