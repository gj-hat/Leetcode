"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/25 16:42
 @description：   剑指 Offer 40. 最小的k个数
 @modified By：
 @version:     1.0
"""

from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]



if __name__ == '__main__':
    arr = [3, 2, 1]
    k = 2
    re = Solution().getLeastNumbers(arr, k)
    print(re)
