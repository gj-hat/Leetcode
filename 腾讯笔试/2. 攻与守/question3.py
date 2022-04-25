"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/24 20:44
 @description：攻与守
 @modified By：
 @version:     1.0
"""

# todo: 攻与守  时间复杂度过高 应该使用哈希表去重


def score_Num(nums, n):
    count1 = 0
    for i in range(1, n + 1):
        if nums[i - 1] == '0':
            count1 += i
    count2 = 0
    for i in range(n + 1, len(nums) + 1):
        if nums[i - 1] == '1':
            count2 += i
    return abs(count1 - count2)


def solve(sum_per, temp):
    per_list = temp
    # 保存结果集
    res = []
    for i in range(sum_per):
        # 绝对值
        res.append(score_Num(per_list, i))
    if res:
        return min(res)
    else:
        return 0


if __name__ == '__main__':
    # 总人数
    sum_per = int(input())
    temp = input()
    if sum_per == 1:
        print(1)
    elif sum_per == 0:
        print(0)
    else:
        a = solve(sum_per, temp)
        print(a)
