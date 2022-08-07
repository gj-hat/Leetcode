"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/7/26 14:16
 @description：  完全二叉树的实现  (不排序)
 @modified By：  广度优先遍历BFS   深度优先遍历DFS
 @version:     1.0
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    def is_empty(self):
        return self.root is None

    # -------------新增节点 广度优先--------------------------------------------------------------
    def add(self, data):
        # 如果根节点的值是空 则直接写入根节点
        if self.root is None:
            self.root = data
            return
        node = TreeNode(data)
        queue = [self.root]
        # 层次遍历  广度优先遍历
        while queue is not None:
            current = queue.pop(0)
            if current.left is None:
                current.left = node
                return
            elif current.right is None:
                current.right = node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    # -------------遍历 直接打印--------------------------------------------------------------
    """
    广度优先遍历直接打印
    """

    def breadth(self):
        if self.root is None:
            print("")
            return
        queue = [self.root]
        while len(queue) != 0:
            current = queue.pop(0)
            print(current.val, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    """
    深度优先遍历直接打印:  先序 中序 后序
    """

    def preorder(self, root: TreeNode):
        if root is None:
            return
        print(root.val, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root: TreeNode):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def postorder(self, root: TreeNode):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=" ")

    # -------------遍历 返回数组--------------------------------------------------------------

    """
    广度优先遍历为数组
    首先观察返回值格式为一个二维数组，
    第 i 行表示二叉树的第 i 层，可以使用队列来协助进行层序遍历，
    队列每一次也传入一个一维数组[ node, level]，
    其中node表示二叉树的节点，level表示该节点所处的层数，
    每遍历至一个节点就将该节点的左右子节点信息存入队列中去，再从队列中取出一组信息，依次循环。
    """

    def breadth_list(self) -> List:
        result = [[]]
        queue = []
        if self.root is None:
            return []
        queue.append([self.root, 0])  # 第一个数据为节点 第二个为层数
        while len(queue) != 0:
            temp = queue.pop(0)
            node: TreeNode = temp[0]  # 节点
            level = temp[1]  # 层数
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left is not None:
                queue.append([node.left, level + 1])
            if node.right is not None:
                queue.append([node.right, level + 1])
        return result


if __name__ == '__main__':
    head = TreeNode(1)
    t = Tree(head)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.inorder(head)  # 4 2 5 1 6 3 7
    print()
    t.breadth()  # 4 2 5 1 6 3 7
    print()
    print(t.breadth_list())
