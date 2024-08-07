#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 16:22
# @Author  : sunaolin
# @File    : 32_4.py

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0]*(len(s)+1)
        for i in range(1,len(s)):
            if s[i]=="(":
                dp[i+1]=0
            else:
                if s[i-1]=="(":
                    dp[i+1]=2+dp[i-1]
                else:
                    if i-dp[i]-1>=0 and s[i-dp[i]-1]=="(":
                        dp[i+1]=2+dp[i]+dp[i-dp[i]-1]
                    else:
                        dp[i+1]=0
        print(dp)
        return max(dp)
