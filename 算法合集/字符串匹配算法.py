"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/11 09:30
 @description：  字符串匹配算法   文本编辑器的查找主要用的是BM算法
 @modified By：
 @version:     1.0
"""


# bf算法
def brute_force(st1, st2):
    """
    本质上是暴力穷举   st1中逐个匹配st2
    :param st1:
    :param st2:
    :return:
    """
    st1_len = len(st1)
    st2_len = len(st2)
    for i in range(st1_len - st2_len):
        if st1[i:i + st2_len] == st2:
            return True
    return False


# bm算法
def boyer_moore(st1, st2):
    """
    坏字符:  坏字符的位置 -  坏字符在模式串中上一次出现的位置
    好后缀:  好后缀的位置 -  好后缀在模式串中上一次出现的位置
    """
    pass


# kmp算法 用的比较少  性能不如bm算法
def knuth_morris_pratt(st1, st2):

    pass



if __name__ == '__main__':
    st1 = "abcdefg"
    st2 = "cde"
    res = brute_force(st1, st2)
    print(res)
