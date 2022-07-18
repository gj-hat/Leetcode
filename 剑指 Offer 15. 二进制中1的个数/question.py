"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 15. 二进制中1的个数
 @modified By：
 @version:     1.0
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        re = bin(n)
        return len(re.split('1')) - 1


if __name__ == '__main__':
    numbers = 11
    re = Solution().hammingWeight(numbers)
    print(re)
