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
        res = []
        if root is None:
            return 0
        qu = [root]
        while len(qu) != 0:
            temp = qu.pop(0)
            res.append(temp.val)
            if temp.left is not None:
                qu.append(temp.left)
            if temp.right is not None:
                qu.append(temp.right)
        res.sort(reverse=True)
        return res[k - 1]


if __name__ == '__main__':
    head = TreeNode(1)
    import tree

    t = tree.Tree(head)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    # t.inorder(head)  # 4 2 5 1 6 3 7
    # print()
    # t.breadth()  # 4 2 5 1 6 3 7
    # print()
    # print(t.breadth_list())

    a = Solution().kthLargest(head, 3)
    print(a)
