#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 12:37
# @Author  : sunaolin
# @File    : 118_2.py


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp=[0]*numRows
        dp[0]=1
        res=[]
        for i in range(numRows):
            for j in range(1,i+1)[::-1]:
                dp[j]=dp[j]+dp[j-1]
            res.append(dp[:i+1])
        return res

