
class Solution:
    def question(self, n ,n1, n2):
        res = ''
        for i in range(n):
            res += n1[i] + n2[i]
        return res


if __name__ == '__main__':
    # 输入数字n
    n = int(input())
    # 输入字符串n1
    n1 = input()
    # 输入字符串n2
    n2 = input()
    # 创建对象
    s = Solution().question(n, n1, n2)
    print(s)





