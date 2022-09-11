"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/8/20 14:57
 @description：
 @modified By：
 @version:     1.0
"""
class Solution:
    def question(self, arr, k):
        n = len(arr)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] + arr[j]) % k == 0:
                    res.append((arr[i], arr[j]))
        return res



if __name__ == '__main__':
    a