#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 14:03
# @Author  : sunaolin
# @File    : 746_1.py

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<=2:
            return min(cost)

        dp=[0]*(len(cost)+1)
        dp[0]=0
        dp[1]=min(cost[:2])
        dp[2]=min(cost[:2])
        for i in range(3,len(dp)):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]
