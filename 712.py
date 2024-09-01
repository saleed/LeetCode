#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/12 19:08
# @Author  : sunaolin
# @File    : 712.py


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]


        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    dp[0][0]=0
                elif i==0:
                    dp[i][j]=dp[i][j-1]+ord(s2[j-1])
                elif j==0:
                    dp[i][j]=dp[i-1][j]+ord(s1[i-1])
                else:
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
                    else:
                        dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))


            print(dp[i])
        return dp[-1][-1]
