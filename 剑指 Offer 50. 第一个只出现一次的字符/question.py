"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 50. 第一个只出现一次的字符
 @modified By：
 @version:     1.0
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        li = dict()
        for i in s:
            j = 1
            if li.get(i) is not None:
                li[i] = j + li.get(i)
            else:
                li[i] = j

        for key, val in li.items():
            if val == 1:
                return key
                # re += key
        return ' '


if __name__ == '__main__':
    s = "leetcode"

    re = Solution().firstUniqChar(s)
    print(re)
