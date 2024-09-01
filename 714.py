#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/12 20:15
# @Author  : sunaolin
# @File    : 714.py

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """


        dp = [[0 for _ in range(2)] for _ in range(len(price))]

        ####定义dp[i][0]表示未持有的时候的最大收益
        ####定义dp[i][1]表示持有的时候的最大收益
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]-fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]-fee)
        return dp[-1][0]

