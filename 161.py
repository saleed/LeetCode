#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 10:05
# @Author  : sunaolin
# @File    : 161.py


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)==len(t):
            diff=0
            for i in range(len(s)):
                if s[i]==t[i]:
                    continue
                diff+=1
            return diff==1
        elif abs(len(s)-len(t))==1:
            p=0
            q=0
            diff=0
            while p<len(s) and q<len(t):
                if s[p]==t[q]:
                    p+=1
                    q+=1
                else:
                    if diff:
                        return False
                    else:
                        diff=1
                        if len(s)>len(t):
                            p+=1
                        else:
                            q+=1

            return True
        else:
            return False




   ##超内存
    def dp(self,s,t):
        dp=[[ float("inf") for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            for j in range(len(t)+1):
                if i==0 and j==0:
                    dp[i][j]=0
                elif i==0:
                    dp[i][j]=dp[i][j-1]+1
                elif j==0:
                    dp[i][j]=dp[i-1][j]+1
                else:
                    if s[i-1]==t[j-1]:
                        dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
                    else:
                        dp[i][j]=min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]+1)
        return dp[-1][-1]==1



