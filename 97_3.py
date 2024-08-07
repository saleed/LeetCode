#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 18:31
# @Author  : sunaolin
# @File    : 97_3.py

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False

        dp=[[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=True if dp[i][j-1] and s2[j-1]==s3[i+j-1] else False
                elif j==0:
                    dp[i][j]=True if dp[i-1][j] and s1[i-1]==s3[i+j-1] else False
                else:
                    dp[i][j]=True if (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1]) else False
            print(dp[i])
        return dp[-1][-1]
