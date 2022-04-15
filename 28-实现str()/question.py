"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/15 09:25
 @description：实现str()
 @modified By：
 @version:     1.0
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 目标字符串为空
        if needle == '':
            return 0
        tar_size = len(needle)
        hay_size = len(haystack)
        # 目标字符串大于原字符串
        if tar_size > hay_size:
            return -1
        # 目标字符串 == 原字符串长度
        elif tar_size == hay_size:
            return 0 if haystack == needle else -1
        else:
            for i in range(hay_size-tar_size+1):
                if haystack[i:i + tar_size] == needle:
                    return i
            return -1



if __name__ == '__main__':
    # haystack = "hello"
    haystack = "abc"

    # needle = "ll"
    needle = "c"
    a = Solution().strStr(haystack, needle)
    print(a)
