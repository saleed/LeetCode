#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 12:41
# @Author  : sunaolin
# @File    : 119_4.py


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp=[0]*(rowIndex+1)
        dp[0]=1
        for i in range(rowIndex+1):
            for j in range(1,i+1)[::-1]:
                dp[j]=dp[j]+dp[j-1]
        return dp