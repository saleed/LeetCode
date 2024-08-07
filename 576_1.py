#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 14:16
# @Author  : sunaolin
# @File    : 576_1.py

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp=[[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove+1)]
        res=0
        for i in range(1,maxMove+1):
            for j in range(m):
                for k in range(n):
                    if i==1:
                        if j==0:
                            dp[i][j][k]+=1
                        if k==0:
                            dp[i][j][k]+=1
                        if j==m-1:
                            dp[i][j][k]+=1
                        if k==n-1:
                            dp[i][j][k]+=1
                    else:
                        # dp[i][j][k]=dp[i-1][j][k]
                        if j-1>=0:
                            dp[i][j][k]+=dp[i-1][j-1][k]
                        if k-1>=0:
                            dp[i][j][k]+=dp[i-1][j][k-1]
                        if j+1<m:
                            dp[i][j][k] += dp[i - 1][j+1][k]
                        if k+1<n:
                            dp[i][j][k] += dp[i - 1][j][k+1]

                        dp[i][j][k] = dp[i][j][k] % (pow(10, 9) + 7)


            res=(res+dp[i][startRow][startColumn])%(pow(10,9)+7)



        return res




