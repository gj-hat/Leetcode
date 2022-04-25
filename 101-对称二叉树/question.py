"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/1 11:03
 @description：  对称二叉树
 @modified By：   https://www.bilibili.com/video/BV1eg411w7gn?p=28
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
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.deppCheck(root.left, root.right)


    def deppCheck(self, left, right):
        """
        递归处理:
        观察可发现: 左子树的左节点和右子树的右节点  左子树的右节点和右子树的右节点 持续递归相等即可
        即 每次递归都 左右子树分别递归
        递归出口:
        1. 左右子树有任何一个为空 则说明不对称
        2. 左右子树的节点对称节点不相同也 说明不对称
        3. 左右子树一直递归到同时为空时  递归结束 说明对称
        :param left:
        :param right:
        :return:
        """

        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.deppCheck(left.left, right.right) and self.deppCheck(left.right, right.left)


if __name__ == '__main__':
    node = tree.Node()
    tree_node = tree.Tree(node)
    # t = [1, 2, 2, 3, 4, 4, 3]
    t = [1,2,2,None,3,None,3]

    for i in t:
        tree_node.add(i)

    # tree_node.breadth_travel()

    b = Solution().isSymmetric(node)
    print(b)
    # a = Solution().isSymmetric(node)
    # print(a)
