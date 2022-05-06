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
        if len(prices) < 2:
            return 0
        min_val = prices[0]
        res = 0
        for i in range(1, len_prices):
            min_val = prices[i] if prices[i] < min_val else min_val       # 记录历史最小的元素
            res = (prices[i] - min_val) if (prices[i] - min_val) > res else res    # 记录当前最大值  (当前元素-历史最小  和  之前最大值-历史最小)
        return res

    def maxProfit2(self, prices: list):
        """
        很高级 动态规划 但是效率不如上面的
        :param prices:
        :return:
        """
        pr_li = len(prices)
        if pr_li < 2:
            return 0
        # 二维数组 prices * 两列
        # 第一列表示当天不持股的利润  第二列表示当天持股的利润
        dp = [[0, 0] for _ in range(pr_li)]
        # 第一天不持股 没有利润  持股 利润为-
        dp[0] = [0, prices[0]*(-1)]
        for i in range(1, pr_li):  # 从第二天开始
            # 当天不持股的利润 = 上一天不持股和 上一天持股+当天的价格  取最大值
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # 当天不持股的利润 = 上一天持股的利润和 当天的价格的负数(即今天第一天持股)  取最大值
            dp[i][1] = max(dp[i-1][1], prices[i] * (-1))

        return max([item for sublist in dp for item in sublist])







if __name__ == '__main__':
    # prices = [7, 6, 4, 3, 1]
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 1, 2, 5, 3, 6, 4]
    a = Solution().maxProfit1(prices)
    b = Solution().maxProfit2(prices)
    print(a)
    print(b)

    pass
