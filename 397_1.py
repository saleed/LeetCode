#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 20:08
# @Author  : sunaolin
# @File    : 397_1.py


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """



###dp方法超内存

        dp=[0]*(n+1)
        dp[0]=0
        for i in range(2,n+1):
            if i%2==0:
                dp[i]=dp[i/2]+1
            else:
                dp[i] = dp[(i + 1) / 2]+2
                if i>=3:
                    dp[i]=min(dp[i],dp[(i-1)/2]+2)
        # print(range(n+1))
        # print(dp)
        return dp[-1]

