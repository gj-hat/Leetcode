"""
 @author：     JiaGuo
 @emil：       1520047927@qq.com
 @date：       Created in 2022/4/22 19:28
 @description： 买卖股票的最佳时机
 @modified By：
 @version:     1.0
"""


class Solution:
    def maxProfit(self, prices):
        """
        没什么讲的  暴力
        :param prices:
        :return:
        """
        price_len = len(prices)
        res = 0
        for i in range(price_len - 1):
            if prices[i + 1] < prices[i]:
                continue
            for j in range(i + 1, price_len):
                temp = prices[j] - prices[i]
                res = temp if res < temp else res
        return res if res > 0 else 0

    def maxProfit1(self, prices):
        """
        高级一点  双指针
        :param prices:
        :return:
        """
        len_prices = len(prices)
        if len(prices) <= 1:
            return 0
        min_val = prices[0]
        res = 0
        for i in range(1, len_prices):
            min_val = prices[i] if prices[i] < min_val else min_val       # 记录历史最小的元素
            res = (prices[i] - min_val) if (prices[i] - min_val) > res else res    # 用当前的减去历史最小元素

        return res


if __name__ == '__main__':
    # prices = [7, 6, 4, 3, 1]
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 1, 2, 5, 3, 6, 4]
    a = Solution().maxProfit1(prices)
    print(a)

    pass
