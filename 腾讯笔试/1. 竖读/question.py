"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/24 20:01
 @description：竖读
 @modified By：
 @version:     1.0
"""

if __name__ == '__main__':

    sum_len = int(input())

    in_li = []
    for i in range(sum_len):
        t = input()
        in_li.append(t)

    val_len = len(in_li[0])
    # 取每个字符串首字母合并成新数组
    out_li = []
    for i in range(val_len):
        out_li.append(in_li[0][i])
        for j in range(1, sum_len):
            out_li[i] += in_li[j][i]
    # 数组每一项变为int
    for i in range(len(out_li)):
        out_li[i] = int(out_li[i])
    out_li.sort()

    for i in out_li:
        print(i, end=" ")
