"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 14:57
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, arr) -> int:
        ans = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n):
            for k in range(j + 1, n):
                if arr[j] > arr[k]:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
            for k in range(arr[j], 1001):
                total[k] += 1

        return ans


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    a = Solution().question(nums)
    print(a)
