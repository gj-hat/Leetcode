def longestStr(s):
    sum = []
    site = 0
    for i in s[0:]:
        temp = 1
        site += 1
        for j in s[site:]:
            temp += 1
            if i == j:
                sum.append(temp)
                break
            else:
                continue
    maxNum = max(sum)
    return maxNum


if __name__ == '__main__':
    str = "abcabcbbbcdea"
    longestNum = longestStr(str)
    print(longestNum)
