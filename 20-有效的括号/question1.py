import time

class Solution:
    def isValid(self, s) -> bool:
        res_list = []
        for i in s:
            if i == '{' or i == '[' or i == '(':
                res_list.append(i)
            else:
                # 排除初始值就不正确的情况
                if res_list == [] and (i[-1] == "}" or i[-1] == "]" or i[-1] == ")"):
                    return False
                if i == "}" and res_list[-1] == "{":
                    res_list.pop()
                elif i == "]" and res_list[-1] == "[":
                    res_list.pop()
                elif i == ")" and res_list[-1] == "(":
                    res_list.pop()
                else:
                    # 出口
                    return False
        return res_list == []


if __name__ == '__main__':
    start = time.time()
    # str = "{{[]}()[]{}}"
    # str = "(])"
    str = "]"
    # str = "{{)}}"

    a = Solution().isValid(str)
    print(a)

    stop = time.time()
    print(f"用时:", stop - start)
