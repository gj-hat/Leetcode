"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/9/9 19:23
 @description：
 @modified By：
 @version:     1.0
"""

if __name__ == '__main__':
    in1 = input()
    print(True if ((len(in1) == 2) and (0 < int(in1[0]) <= 9) and (in1[1] in ['C', 'D', 'H', 'S'])) or (
                (len(in1) == 3) and (0 < int(in1[0:2]) <= 13) and (
                    in1[2:len(in1) + 1] in ['C', 'D', 'H', 'S'])) else False)
