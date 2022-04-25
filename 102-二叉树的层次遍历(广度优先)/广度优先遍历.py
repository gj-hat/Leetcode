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
    def breadth_travel(self, root) -> list:
        if root is None:
            return []
        current = [root]         # 将root节点初始化为current
        res = []                 # 结果数组
        next = []               # 下一层暂存  下一层的左右孩子
        tmp_val = []              # 每一层数组
        while current:                       # 当前数组不为空
            tmp = current.pop(0)       # 当前数组中 队首元素出队
            tmp_val.append(tmp.val)             # 上面队首元素的值 入每一层的数组队列
            if tmp.left is not None:              # 左孩子不为空
                next.append(tmp.left)               # next数组中添加左孩子
            if tmp.right is not None:             # 右孩子不为空
                next.append(tmp.right)               # next数组中添加右孩子
            if not current:                      # 当前为空时候
                if not next:                        # next为空
                    if tmp_val:                       # 每一层的数组不为空
                        res.append(tmp_val)            # 结果数组中添加每一层的元素
                    return res
                else:
                    current = next                       # 指针后移  current = next
                    next = []                             # next值为空
                res.append(tmp_val)                       # 结果数组中添加每一层的元素
                tmp_val = []                                # 每一层置为空



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
