"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/31 13:52
 @description：  二叉树的中序遍历
 @modified By：
 @version:     1.0
"""

import tree
import time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    # 广度优先遍历
    def preorderTraversal(self, root):
        if root is None:
            return self.res
        self.res.append(root.data)
        self.preorderTraversal(root.lchild)
        self.preorderTraversal(root.rchild)
        return self.res






if __name__ == '__main__':
    node = tree.Node()
    tree_node = tree.Tree(node)
    tree_node.add(0)
    tree_node.add(1)
    tree_node.add(2)
    tree_node.add(3)
    tree_node.add(4)
    tree_node.add(5)

    # tree_node.breadth_travel()






    a = Solution().preorderTraversal(node)
    print(a)
