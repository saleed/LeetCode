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
        dp=[[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0]=-prices[0]
        dp[0][1]=0
        dp[0][2]=0 ##这个状态
        maxv=0

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2]-prices[i])
            dp[i][1]=dp[i-1][0]+prices[i]
            dp[i][2]=max(dp[i-1][1],dp[i-1][2])
            maxv=max(maxv,max(dp[i]))

        return maxv