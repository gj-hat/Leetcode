"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 54. 二叉搜索树的第k大节点
 @modified By：
 @version:     1.0
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        nodeSet = dict()
        resList = self.toList(root, nodeSet)
        resList.reverse()
        return resList[k]


    def toList(self, root: TreeNode, nodeSet) -> List:
        current = root
        if current.left.val is None:
            return
        if current.right.val is None:
            return




        return []



if __name__ == '__main__':
    nums = [0, 1]

    re = Solution().kthLargest(TreeNode(1), 1)
    print(re)
