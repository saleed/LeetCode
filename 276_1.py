#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 16:57
# @Author  : sunaolin
# @File    : 276_1.py


###涂相同颜色 涂不同颜色两种情况

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        dp=[[0 for _ in range(2)] for _ in range(n)]

        dp[0][0]=k #不同颜色
        dp[0][1]=0 #相同颜色

        for i in range(1,n):
            dp[i][0]=sum(dp[i-1])*(k-1)
            dp[i][1]=dp[i-1][0]
            print(dp[i])
        return sum(dp[-1])
