#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 16:41
# @Author  : sunaolin
# @File    : 516_1.py

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[[0 for _ in range(len(s))] for _ in range(len(s))]
        maxl=0

        for itv in range(len(s)):
            for i in range(len(s)):
                if i+itv>=len(s):
                    continue
                if itv==0:
                    dp[i][i+itv]=1
                elif itv==1:
                    dp[i][i+itv]=2 if s[i]==s[i+itv] else 1
                else:
                    dp[i][i+itv]=dp[i+1][i+itv-1]+2 if s[i]==s[i+itv] else max(dp[i][i+itv-1],dp[i+1][i+itv])
                maxl=max(maxl,dp[i][i+itv])

        for v in  dp:
            print(v)

        return maxl


s ="abcabcabcabc"
a=Solution()
print(a.longestPalindromeSubseq(s))

