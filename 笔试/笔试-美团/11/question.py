"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/6 14:44
 @description：  三元组
 @modified By：
 @version:     1.0
"""

class Solution:
    def question(self, num, nums):
        lens = len(nums)
        if lens < 3:
            return 0
        # res = []
        # temp = []
        count = 0
        for i in range(0, lens):
            for j in range(i+1, lens):
                for k in range(j+1, lens):
                    if nums[i] - nums[j] == 2 * nums[j] - nums[k]:
                        count += 1
        return count

if __name__ == '__main__':
    # 输入一个数字
    num = int(input())
    # 输入一组数字按空格分隔
    nums = input().split()
    # 将输入的数字转换为整型
    nums = [int(i) for i in nums]

    # num = 4
    # nums = [4, 2, 2, 2]

    s = Solution().question(num, nums)
    print(s)
