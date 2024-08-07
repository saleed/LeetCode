#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 19:30
# @Author  : sunaolin
# @File    : 139_1.py


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[-1]


