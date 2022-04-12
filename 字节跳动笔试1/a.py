"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/3/27 19:48
 @description：
 @modified By：
 @version:     1.0
"""

"""
广告算法  一本书中有n页  有m种广告设计方案  让你输出每一个设计方案是否合理(1/0) 结果空格输出
方案合理性要求:   两个广告之间必须间隔k页
m的数据格式:  m是一个n项数列  数列的每一个元素代表相应页码是否有广告

例如:
    输入:
        第一行      5 2 2     表示这本书有5页   两种广告设计方案  广告之间必须间隔两页
        第二行      1 0 0 1 1          表示方案一  第一页 第四页 第五页有广告  下标对应页数有广告为1无广告为0
        第三行      1 0 0 1 0          表示方案二  第一页  第四页有广告
    输出:
        0 1      表示方案一不合理 方案二合理
"""


def fun(n, m, k, li):
    """
    :param n: 每一个数组的个数
    :param m: 有多少个数组
    :param k: 间隔的数量
    :param li: 数组的数值 二维
    :return:
    """
    res = list()
    for ii in range(m):
        if (n - k) <= 0:
            if search_count(1, li[ii][0: m]) <= 1 <= 1:
                res.append(1)
            else:
                res.append(0)
        else:
            tempp = 1
            for j in range(n - k):
                if search_count(1, li[ii][j: j + k + 1]) > 1:
                    tempp = 0
            res.append(0 if tempp == 0 else 1)
    for i in res:
        print(i, end=" ")


def search_count(s, li):
    num = 0
    for _ in li:
        if _ == s:
            num += 1
    return num


if __name__ == '__main__':
    in_num = input().split(" ")
    in_num = list(map(int, in_num))
    n = in_num[0]
    m = in_num[1]
    k = in_num[2]
    in_list = [[] * n for _ in range(m)]
    for i in range(m):
        temp = input().split(" ")
        in_list[i] = list(map(int, temp))
    fun(n, m, k, in_list)
