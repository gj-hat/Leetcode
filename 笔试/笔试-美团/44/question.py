"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 10:08
 @description： 斐波那契数列
 @version:     1.0
"""


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


    def breadth_list(self):
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


def aaaa(head: TreeNode):
    current_head = head

    dphead = TreeNode(head.val)
    dp = Tree(dphead)

    dp.add(current_head.left.val)
    dp.add(current_head.right.val)





    # for i in range(2, n+1):


    dp[i] = max(dphead.left.val + current_head.val, dphead.left.val)


    return dp[-1]


if __name__ == '__main__':

    num = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]

    head = TreeNode(nums[0])
    headTool = Tree(head)
    for i in nums[1::]:
        headTool.add(i)
    a = aaaa(num, head)



