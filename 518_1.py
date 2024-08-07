#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 17:36
# @Author  : sunaolin
# @File    : 518_1.py

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount + 1):
                if i == 0:
                    dp[i][j] = 1 if j % coins[0] == 0 else 0  ##因为是组合所以这里是j%coins[0]
                else:
                    for k in range(j // coins[i] + 1):
                        dp[i][j] += dp[i - 1][j - k * coins[i]]
            print(dp[i])
        return dp[-1][-1]
