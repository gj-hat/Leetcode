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

    def __init__(self, data=None):
        self.data = data
        self.lchild = None  # 左节点
        self.rchild = None  # 右节点


class Tree:
    """ 二叉树 """
    def __init__(self):
        """ 根节点 """
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, item):
        """ 插入操作(尾插) 广度优先(层次)遍历 底层原理是队列"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]  # 队列
        while queue:  # 列表为空则跳出循环
            cur_node = queue.pop(0)  # 队列中取出元素  以队列的原理出队列只能是首节点
            if cur_node.lchild is None:  # 左节点是否为空  为空直接挂上去就好
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)  # 左孩子不为空 则入队列
            if cur_node.rchild is None:  # 右节点是否为空  为空直接挂上去就好
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)  # 右孩子不为空 则入队列


    def breadth_travel(self):
        """
        广度优先遍历/层次遍历      底层原理队列
        :return:
        """
        if self.root is None:
            print("空")
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data, end=" ")
            if cur_node.lchild is not None:  # 左节点是否为空  不为空添加进队列中
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:  # 右节点是否为空  不为空添加到队列中
                queue.append(cur_node.rchild)




    def preorder_travel(self, node):
        """
        深度遍历   先序
        :param node:
        :return:
        """
        if node is None:   # 递归出口 当节点为None时退出
            return
        print(node.data, end=" ")
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)



    def inorder_travel(self, node):
        """
        深度遍历   中序
        :param node:
        :return:
        """
        if node is None:   # 递归出口 当节点为None时退出
            return
        self.inorder_travel(node.lchild)
        print(node.data, end=" ")
        self.inorder_travel(node.rchild)


    def postorder_travel(self, node):
        """
        深度遍历   后序
        :param node:
        :return:
        """
        if node is None:   # 递归出口 当节点为None时退出
            return
        self.postorder_travel(node.lchild)
        self.postorder_travel(node.rchild)
        print(node.data, end=" ")


    def is_full(self):
        pass


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder_travel(tree.root)
    print(" ")
    tree.inorder_travel(tree.root)
    print(" ")
    tree.postorder_travel(tree.root)
    print(" ")
