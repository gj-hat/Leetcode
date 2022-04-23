"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/23 10:35
 @description：多数元素
 @modified By：
 @version:     1.0
"""


class Solution:
    def majorityElement(self, nums) -> int:
        """
        不可取 暴力
        :param nums:
        :return:
        """
        nums_len = len(nums)
        res_len = nums_len / 2
        res_dict = dict()
        for i in nums:
            if res_dict.get(i):
                res_dict[i] += 1
            else:
                res_dict[i] = 1
        for k, v in res_dict.items():
            if v >= res_len:
                return k

    def majorityElement1(self, nums) -> int:
        """
        摩尔投票法   详情见md   必须得超过一半
        :param nums:
        :return:
        """
        major, count = 0, 0
        for ii in nums:
            if count == 0:
                major = ii
            if ii == major:
                count += 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    a = Solution().majorityElement1([3, 3, 4, 4, 5, 5, 4, 5, 5, 5])

    print(a)
    pass
