"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   784-字母大小写全排列(回溯)
 @modified By：
 @version:     1.0
"""


from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        digits = s
        slen = len(s)

        if slen == 0:
            return []

        def backtrack(index: int):
            if index == slen:
                combinations.append("".join(combination))
            elif digits[index].isdigit():
                combination.append(digits[index])
                backtrack(index + 1)
                combination.pop()
            else:
                digit = digits[index]
                digit_words = [digit.lower(), digit.upper()]
                for i in digit_words:
                    combination.append(i)
                    backtrack(index + 1)
                    combination.pop()


        combinations = []
        combination = []
        backtrack(0)


        return combinations

if __name__ == '__main__':
    s = "a1b2"
    a = Solution()
    aa = a.letterCasePermutation(s)
    print(aa)


