#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/22 18:07
# @Author  : sunaolin
# @File    : 72——3.py


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i==0 and j==0:
                    continue
                elif i==0:
                    dp[i][j]=dp[i][j-1]+1
                elif j==0:
                    dp[i][j]=dp[i-1][j]+1
                else:
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
                    else:
                        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,dp[i-1][j-1]+1)
        return dp[-1][-1]
