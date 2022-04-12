"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/31 09:17
 @description：  字符串解码
 @modified By：      https://www.bilibili.com/video/BV1eg411w7gn?p=22&spm_id_from=333.851.header_right.history_list.click
 @version:     1.0
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        for i in s:
            if i == '[':  # 当元素等于  左中括号    如果有中间变量先把中间变量append
                if num != 0:
                    stack.append(num)
                stack.append(i)
                num = 0
            elif i.isdigit():  # 当元素等于  数字时 暂存入中间变量中(防止多位数的情况)
                num = num * 10 + int(i)


            elif i == ']':  # 当元素等于  右中括号   循环出栈 取出上一个左括号里的元素
                temp = []
                while stack[-1] != '[':
                    st = stack.pop()
                    temp.append(st)
                stack.pop()  # 取出左中括号
                num = stack.pop()  # 取出 左中括号前的数字
                ss = temp[::-1] * int(num)  # 计算出解码后的元素
                stack.extend(ss)  # 将解码后的元素入栈
                num = 0  # 中间变量置为0

            else:
                stack.append(i)  # 加密的元素 即字母  入栈
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("30[a]2[bc]"))
    print(solution.decodeString("3[a2[c]]"))
    print(solution.decodeString("2[abc]3[cd]ef"))
