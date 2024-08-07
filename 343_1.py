#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 19:50
# @Author  : sunaolin
# @File    : 343_1.py

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0]=1

        for i in range(n+1):
            for j in range(1,i):
                # dp[i]=max(dp[i],dp[j]*(i-j))  ######错误写法
                dp[i] = max(dp[i], max(dp[j], j) * (i - j))
        return dp[-1]

