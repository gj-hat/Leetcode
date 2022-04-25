"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/23 12:38
 @description：合并二叉树
 @modified By：
 @version:     1.0
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        return root1 or root2



    def breadth_travel(self, root: TreeNode) -> list:  # [2,1,3,null,4,null,7]
        """
                2
            1       3
       null   4   null  7
        """
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left is not None:  # 左节点是否为空  不为空添加进队列中
                queue.append(cur.left)
            if cur.right is not None:  # 右节点是否为空  不为空添加到队列中
                queue.append(cur.right)
        return res

    def breadth_add(self, val, root: TreeNode) -> TreeNode:
        newNode = TreeNode(val)
        temp_li = [root]
        if root is None:
            return newNode
        while temp_li is not None:
            current = temp_li.pop(0)
            if current.left is None:
                current.left = newNode
                return root
            if current.right is None:
                current.right = newNode
                return root
            temp_li.append(current.left)
            temp_li.append(current.right)


if __name__ == '__main__':

    a = Solution()
    nu1 = [1, 3, 2, 5]
    nu2 = [2, 1, 3, None, 4, None, 7]
    node1 = TreeNode(nu1[0])
    node2 = TreeNode(nu2[0])
    for i in nu1[1::]:
        a.breadth_add(i, node1)
    for i in nu2[1::]:
        a.breadth_add(i, node2)


    cc = Solution().mergeTrees(node1, node2)


    aa = Solution().breadth_travel(cc)
    print(aa)

