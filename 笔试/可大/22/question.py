"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 14:57
 @description：
 @modified By：
 @version:     1.0
"""

class Solution:
    def signalVerify(self , signal: str) -> bool:
        res = False
        # str以空格分开
        signal = signal.split("=")
        # 多个空格错
        if len(signal) != 2:
            return res
        # signal[0]长度为1且只能是小写字母
        if len(signal[0]) != 1 or not signal[0].islower():
            return res
        # signal[1]以空格开头
        if signal[1][0] == " ":
            return res
        # signal[1]只能是小写字母数字和空格
        for i in signal[1]:
            if not i.islower() and not i.isdigit() and i != " ":
                return res
        return True



if __name__ == '__main__':
    a = Solution().signalVerify('a=0 0')
    print(a)
