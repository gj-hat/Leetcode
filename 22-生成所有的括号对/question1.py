import time


def fun(n: int) -> list:
    solutionMap = {}
    # 记录下n=0和1时的答案
    solutionMap[0] = [""]
    solutionMap[1] = ["()"]

    # 遍历小于n的所有长度
    for i in range(2, n + 1):
        cur = set()
        # 遍历小于n的所有长度
        for j in range(1, i):
            # 构造答案
            ans1 = solutionMap[j]
            ans2 = solutionMap[i - j]
            for s in ans1:
                for t in ans2:
                    cur.add(s + t)
        # 构造 ( solution(n-1) )这种答案
        for s in solutionMap[i - 1]:
            cur.add("(" + s + ")")
        solutionMap[i] = cur
    return list(solutionMap[n])


if __name__ == '__main__':
    start = time.clock()
    print(fun(3))
    stop = time.clock()
    print(f"用时:", stop - start)
