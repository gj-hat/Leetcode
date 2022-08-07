"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/7 10:59
 @description：  17. 电话号码的字母组合(回溯)
 @modified By：      
 @version:     1.0
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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


if __name__ == '__main__':
    digits = "23"
    a = Solution().letterCombinations(digits)
    print(a)
