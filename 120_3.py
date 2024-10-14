#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/4 17:03
# @Author  : sunaolin
# @File    : 120_3.py




class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp=[0]*len(triangle)
        for i in range(len(triangle)):
            for j in range(i+1):
                if j==0:
                    dp[j]=dp[j]+triangle[i][j]
                elif j==i:
                    dp[j]=dp[j-1]+triangle[i][j]
                else:
                    dp[j]=min(dp[j],dp[j-1])+triangle[i][j]
        return min(dp)
