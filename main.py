# 方程式应为 1x + ky = n
# 这里n其实为大边长


n = int(input("请输入n值:"))
k = int(input("请输入k值:"))


def Permutation(num):
    if num == 0:
        return 1
    else:
        return num * Permutation(num - 1)


if __name__ == '__main__':

    # print(Permutation(4))
    a = 0
    for i in range(n + 1):
        if (n - i) % k == 0:
            a += Permutation(i + (n - i) / k) / (Permutation(i) * Permutation((n - i) / k))
        else:
            continue
    print(int(a))
