"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/31 13:52
 @description：  二叉树的中序遍历
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
    # 广度优先遍历
    def inorderTraversal(self, root):
        res = []
        if root is None:
            return res
        cur = root
        queue = [cur]
        count = 1
        while queue:
            temp = []
            cur_node = queue.pop(0)
            if count == 1:
                temp.append(cur_node.val)
                res.append(temp)
                count = 2
                temp = []

            if cur_node.left is not None:
                queue.append(cur_node.left)
                temp.append(cur_node.left.val)

            if cur_node.right is not None:
                queue.append(cur_node.right)
                temp.append(cur_node.right.val)
            res.append(temp)


        return [i for i in res if i != []]

        # return res


    def inorderTraversal1(self, root):
        # todo 没看懂
        if root is None:
            return []
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
                    return res
                else:
                    current = nxt
                    nxt = []
                res.append(tmp_val)
                tmp_val = []



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

    a = Solution().inorderTraversal(node)
    print(a)
