#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 17:55
# @Author  : sunaolin
# @File    : 72_2.py


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[ 0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]


        for i in range(len(word1)+1):
            dp[i][0]=i
        for j in range(len(word2)+1):
            dp[0][j]=j


        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[-1][-1]
