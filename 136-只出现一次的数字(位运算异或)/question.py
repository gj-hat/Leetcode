"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/8 09:21
 @description：  位运算 只出现一次的数字
 @modified By：
 @version:     1.0
"""


class Solution:
    # hashmap  key数组  value 计数

    # 方法二 位运算
    """
    任何一个数 和自己异或一定是0   ^
    所以让数组的每一个数都和自己异或

    按位异或的3个特点:
        (1) 0^0=0,0^1=1 0异或任何数＝任何数
        (2) 1^0=1,1^1=0 1异或任何数－任何数取反
        (3) 任何数异或自己＝把自己置0
        (4) a^b^c^b = a + b + c - b  即没有相同的数字就加上 有相同的就减去


    按位异或的几个常见用途:
        (1) 使某些特定的位翻转
        例如对数10100001的第2位和第3位翻转，则可以将该数与00000110进行按位异或运算。
        　　　　　 10100001^00000110 = 10100111
    """

    def singleNumber(self, nums) -> int:
        res = 0
        for i in nums:
            a = res ^ i
            res = res ^ i

        return res


if __name__ == '__main__':
    li = [4, 9, 2, 9, 2, 4]
    a = Solution()
    b = a.singleNumber(li)
    print(b)
