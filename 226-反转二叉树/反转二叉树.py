"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/1 17:14
 @description：  反转二叉树
 @modified By：
 @version:     1.0
"""

import tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root == None:
            return root
        cur = root
        return self.helper(cur)

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.helper(root.right)
        root.left, root.right = root.right, root.left
        return





if __name__ == '__main__':
    node = tree.Node()
    tree_node = tree.Tree(node)
    # tree_node.add(0)
    # tree_node.add(1)
    # tree_node.add(2)
    # tree_node.add(3)
    # tree_node.add(4)
    nu = [4, 2, 7, 1, 3, 6, 9]
    for i in nu:
        tree_node.add(i)

    # tree_node.add(6)

    # tree_node.breadth_travel()

    a = Solution().invertTree(node)
    b = tree_node.breadth_travel()

    # print(a)
