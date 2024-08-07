#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 19:17
# @Author  : sunaolin
# @File    : 552_1.py

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[0 for _ in range(6)] for _ in range(n)]

        ##按照缺席天数0，,1和迟到记录连续天数0，,1，,2，分成6个状态
        dp[0][0]=1
        dp[0][1]=1
        dp[0][2]=0
        dp[0][3]=1
        dp[0][4]=0
        dp[0][5]=0
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]
            dp[i][1]=dp[i-1][1]+dp[i-1][0]
            dp[i][2]=dp[i-1][2]+dp[i-1][1]
            dp[i][3]=dp[i-1][0]+dp[i-1][3]
            dp[i][4]=dp[i-1][1]+dp[i-1][3]+dp[i-1][4]
            dp[i][5]=dp[i-1][2]+dp[i-1][4]+dp[i-1][5]
        return sum(dp[-1])%(pow(10,9)+7)

