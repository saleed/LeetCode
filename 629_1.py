#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 18:38
# @Author  : sunaolin
# @File    : 629_1.py

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        dp=[[0 for _ in range(int(n*(n+1)/2)+1)] for _ in range(n)]
        dp[1][0]=1
        dp[1][1]=1

        for i in range(2,n):
            for j in range(int(n*(n+1)/2)+1):
                for k in range(i+1):
                    if j-(i-k)>=0:
                        dp[i][j]+=dp[i-1][j-(i-k)]
        return dp[-1][-1]%(pow(10,9)+7)

