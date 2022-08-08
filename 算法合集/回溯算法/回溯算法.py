"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/7 15:14
 @description：
 @modified By：
 @version:     1.0
"""

"""
回溯算法适用于以下的场景。

组合问题：N个数里面按一定规则找出k个数的集合
切割问题：一个字符串按一定规则有几种切割方式
子集问题：一个N个数的集合里有多少符合条件的子集
排列问题：N个数按一定规则全排列，有几种排列方式
棋盘问题：N皇后，解数独等等


"""

"""
回溯算法模板
    1. 回溯函数模板返回值以及参数   (递归函数)
    2. 回溯函数终止条件                 
    3. 回溯搜索的遍历过程

"""


# leetcode 17题目为例
class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []

        phoneMapEnum = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                        "9": "wxyz"}

        # 回溯   index: digits第几个元素
        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMapEnum[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combinations = []
        combination = []
        # 从digits第一个元素开始
        backtrack(0)
        return combinations
