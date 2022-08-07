"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/6 14:44
 @description：数组中的字符串匹配
 @modified By：
 @version:     1.0
"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return []
        res = set()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isSubstring(words[i], words[j]):
                    res.add(words[i])
                if self.isSubstring(words[j], words[i]):
                    res.add(words[j])

        return list(res)

    # 判断字符串中是否包含子串
    def isSubstring(self, s1: str, s2: str) -> bool:
        if s1 in s2:
            return True
        else:
            return False


if __name__ == '__main__':
    words = ["mass", "as", "hero", "superhero"]
    s = Solution()
    aa = s.stringMatching(words)
    print(aa)
