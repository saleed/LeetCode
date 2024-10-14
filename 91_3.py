#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/4 12:18
# @Author  : sunaolin
# @File    : 91_3.py



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0

        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1 if s[0]!='0' else 0
        for i in range(2,len(s)+1):
            if s[i-1]!='0':
                dp[i]=dp[i-1]
            if 1<=int(s[i-2:i])<=26 and s[i-2]!='0':
                dp[i]+=dp[i-2]
        return dp[-1]