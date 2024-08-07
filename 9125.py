#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 20:01
# @Author  : sunaolin
# @File    : 9125.py


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp=[0]*len(s)
        dp[-1]=1 if s[-1]!='0' else 0

        if len(s)>=2:
            if s[-2]=='0':
                dp[-2]=0
            elif 1<=int(s[-2:])<=26:
                dp[-2]=dp[-1]+1
            else:
                dp[-2]=dp[-1]

        for i in range(len(s)-2)[::-1]:
            if s[i]=='0':
                dp[i]=0
                continue
            dp[i]=dp[i-1]
            if 1<=int(s[i:i+2])<=26:
                dp[i]+=dp[i-2]

        return dp[0]

