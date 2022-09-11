"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/27 16:16
 @description：
 @modified By：
 @version:     1.0
"""
import re


class Solution:
    def question(self, num, s, reg):

        s = "aaaa"
        # 删除sv


        son_st = []
        count = 0
        # 将s 划分为长num的子串 放入son_st
        for i in range(len(s) - num + 1):
            son_st.append(s[i:i + num])

        r = reg.split("*")
        for i in son_st:
            if i.startswith(r[0]) and i.endswith(r[1]):
                count += 1
        return count


if __name__ == '__main__':
    inp1 = input().split(" ")
    arr1 = [int(i) for i in inp1]

    S = input()
    ss = input()
    a = Solution().question(arr1[1], S, ss)
    print(a)





