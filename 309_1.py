#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 11:10
# @Author  : sunaolin
# @File    : 309_1.py

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
           我们用f[i]表示第i天结束之后的「累计最大收益」。根据题目描述，由于我们最多只能同时买入（持有）一支股票，
        并且卖出股票后有冷冻期的限制，因此我们会有三种不同的状态：
        1.我们目前持有一支股票，对应的「累计最大收益」记为f[i][0]；
        2.我们目前不持有任何股票，并且该天后一天处于冷冻期，对应的「累计最大收益」记为 f[i][1]；
        3.我们目前不持有任何股票，并且该天后一天不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]。
        """

        dp=[[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0]=-prices[0]  ##持有一支股票
        dp[0][1]=0  ##不持有股票且第1天处于冷冻期
        dp[0][2]=0  ##不持有股票，且第1天不处于冷冻期

        maxv=0

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1]=dp[i-1][0]+prices[i]
            dp[i][2]=max(dp[i-1][1],dp[i-1][2])
            maxv=max(maxv,max(dp[i]))

        return maxv