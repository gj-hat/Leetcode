"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 17. 打印从1到最大的n位数
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, pow(10, n))]


if __name__ == '__main__':
    numbers = 3
    re = Solution().printNumbers(numbers)
    print(re)
