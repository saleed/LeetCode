#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 17:18
# @Author  : sunaolin
# @File    : 279_3.py


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float("inf")]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(1,n+1):
            j=1
            while j*j<=i:
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return  dp[-1]
