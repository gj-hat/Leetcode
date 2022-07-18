"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 05. 替换空格
 @modified By：
 @version:     1.0
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res



if __name__ == '__main__':
    s = "We are happy."
    re = Solution().replaceSpace(s)
    print(re)




