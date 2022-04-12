"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/22 16:10
 @description：   完全二叉树的实现  (不排序)
 @modified By：    广度优先遍历BFS   深度优先遍历DFS
 @version:     1.0
"""


class Node:
    """
    树的节点
    """

    def __init__(self, val=None):
        self.val = val
        self.left = None  # 左节点
        self.right = None  # 右节点


class Tree:
    """ 二叉树 """
    def __init__(self, node=None):
        """ 根节点 """
        self.root = node

    def is_empty(self):
        return self.root is None

    def add(self, item):
        """ 插入操作(尾插) 广度优先(层次)遍历 底层原理是队列"""
        if self.root.val is None:
            self.root.val = item
            return
        node = Node(item)
        queue = [self.root]  # 队列
        while queue:  # 列表为空则跳出循环
            cur_node = queue.pop(0)  # 队列中取出元素  以队列的原理出队列只能是首节点
            if cur_node.left is None:  # 左节点是否为空  为空直接挂上去就好
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)  # 左孩子不为空 则入队列
            if cur_node.right is None:  # 右节点是否为空  为空直接挂上去就好
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)  # 右孩子不为空 则入队列


    def breadth_travel(self):
        """
        广度优先遍历/层次遍历      底层原理队
        :return:
        """
        if self.root is None:
            print("空")
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=" ")
            if cur_node.left is not None:  # 左节点是否为空  不为空添加进队列中
                queue.append(cur_node.left)
            if cur_node.right is not None:  # 右节点是否为空  不为空添加到队列中
                queue.append(cur_node.right)




    def preorder_travel(self, node):
        """
        深度遍历   先序
        :param node:
        :return:
        """
        if node is None:   # 递归出口 当节点为None时退出
            return
        print(node.val, end=" ")
        self.preorder_travel(node.left)
        self.preorder_travel(node.right)



    def inorder_travel(self, node):
        """
        深度遍历   中序
        :param node:
        :return:
        """
        if node is None:   # 递归出口 当节点为None时退出
            return
        self.inorder_travel(node.left)
        print(node.val, end=" ")
        self.inorder_travel(node.right)


    def postorder_travel(self, node):
        """
        深度遍历   后序
        :param node:
        :return:
        """
        if node is None:   # 递归出口 当节点为None时退出
            return
        self.postorder_travel(node.left)
        self.postorder_travel(node.right)
        print(node.val, end=" ")


