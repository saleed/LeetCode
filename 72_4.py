#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/2 15:31
# @Author  : sunaolin
# @File    : 72_4.py


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[0 for _ in range(len(word2))] for _ in range(len(word1))]  ##不过不多留一个空位，会多出来很多判断 仅供参考

        for i in range(len(word1)):
            for j in range(len(word2)):
                if i==0 and j==0:
                    dp[0][0]=0 if word1[0]==word2[0] else 0
                    continue
                v1=dp[i-1][j] if i-1>=0 else float('inf')
                v2=dp[i][j-1] if j-1>=0 else float('inf')
                v3=dp[i-1][j-1] if i-1>=0 and j-1>=0 else float('inf')
                if word1[i]==word2[j]:
                    dp[i][j]=min(v1+1,v2+1,v3)
                else:
                    dp[i][j]=min(v1+1,v2+1,v3+1)
        return dp[-1][-1]
