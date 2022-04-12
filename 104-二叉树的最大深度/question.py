"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/1 15:15
 @description：  二叉树的最大深度
 @modified By：  https://www.bilibili.com/video/BV1eg411w7gn?p=29
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
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        current = [root]
        res = []
        nxt = []
        tmp_val = []
        while current:
            tmp = current.pop(0)
            tmp_val.append(tmp.val)
            if tmp.left is not None:
                nxt.append(tmp.left)
            if tmp.right is not None:
                nxt.append(tmp.right)
            if not current:
                if not nxt:
                    if tmp_val:
                        res.append(tmp_val)
                    return len(res)
                else:
                    current = nxt
                    nxt = []
                res.append(tmp_val)
                tmp_val = []


    """ 递归  """

    def maxDepth1(self, root) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth1(root.left), self.maxDepth1(root.right))+1



if __name__ == '__main__':
    node = tree.Node()
    tree_node = tree.Tree(node)
    tree_node.add(0)
    tree_node.add(1)
    tree_node.add(2)
    tree_node.add(3)
    tree_node.add(4)
    tree_node.add(None)
    tree_node.add(None)
    tree_node.add(5)
    # tree_node.add(6)

    # tree_node.breadth_travel()

    a = Solution().maxDepth1(node)
    print(a)
