#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 12:46
# @Author  : sunaolin
# @File    : 120_2.py


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp=[0]*len(triangle)
        for i in range(len(triangle)):
            if i>0:
                dp[i]=dp[i-1]+triangle[i][-1]  ##一定要最先计算
            for j in range(1,i)[::-1]:
                dp[j]=min(dp[j],dp[j-1])+triangle[i][j]
            dp[0]+=triangle[i][0]

            # print(dp)
        return min(dp)