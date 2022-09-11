"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 10:49
 @description：
 @modified By：
 @version:     1.0
"""


class Solution:
    def question(self, nums, p, score):
        n = nums[1]
        for i in range(n):
            min = p[0]
            index = 0
            for j in range(len(p)):
                if p[j] < min:
                    min = p[j]
                    index = j
            p[index] = 100
        res = 0
        for k in range(len(p)):
            temp = p[k] / 100
            res += temp * score[k]

        return res


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    score = [int(x) for x in input().split()]
    s = Solution().question(nums, p, score)
    print(s)
