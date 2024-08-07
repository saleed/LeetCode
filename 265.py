#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 16:07
# @Author  : sunaolin
# @File    : 265.py



class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dp=[[float("inf") for _ in range(len(costs[0]))] for _ in range(len(costs))]

        for i in range(len(costs[0])):
            dp[0][i]=costs[0][i]

        for i in range(1,len(costs)):
            for j in range(len(costs[0])):
                for k in range(len(costs[0])):
                    if j==k:
                        continue
                    dp[i][j]=min(dp[i][j],dp[i-1][k]+costs[i][j])
        return min(dp[-1])