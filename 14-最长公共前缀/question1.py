import time

"""
中间变量 初始值为[0]
用中间变量和 strs的每一个元素比较   得出中间共同元素 赋值给中间变量

"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        temp_str = strs[0]
        for i in range(1, len(strs)):
            index = 0
            len_list_two = len(strs[i]) if len(strs[i]) <= len(temp_str) else len(temp_str)
            while index < len_list_two and (temp_str[index] == strs[i][index]):
                index += 1
            temp_str = temp_str[:index]
        return str(temp_str)


if __name__ == '__main__':
    start = time.time()

    # strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    strs = ["ab","a"]

    a = Solution().longestCommonPrefix(strs)
    print("a=",a)

    stop = time.time()
    print(f"用时:", stop - start)
