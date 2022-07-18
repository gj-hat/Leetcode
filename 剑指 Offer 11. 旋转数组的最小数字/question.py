"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 11. 旋转数组的最小数字
 @modified By：
 @version:     1.0
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """

        :param numbers:
        :return:
        """
        res = min(numbers)
        return res


if __name__ == '__main__':
    numbers = [3, 4, 5, 1, 2]
    re = Solution().minArray(numbers)
    print(re)

