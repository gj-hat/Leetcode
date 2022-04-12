"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/1 15:15
 @description：  二叉树的最大深度
 @modified By：  https://www.bilibili.com/video/BV1eg411w7gn?p=29
 @version:     1.0
"""
import math

import tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # todo 没看懂
    def isBalanced(self, root) -> bool:
        if root is None:
            return True
        return self.helper(root) != -1

    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right == -1 or math.fabs(right - left) > 1:
            return -1

        return max(left, right) + 1


if __name__ == '__main__':
    node = tree.Node()
    tree_node = tree.Tree(node)
    # tree_node.add(0)
    tree_node.add(1)
    tree_node.add(2)
    tree_node.add(3)
    tree_node.add(4)

    # tree_node.add(6)

    # tree_node.breadth_travel()

    a = Solution().isBalanced(node)
    print(a)
