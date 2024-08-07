#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 16:44
# @Author  : sunaolin
# @File    : 221_4.py


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    dp[i][j]=1 if matrix[i][j]=="1" else 0
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1 if matrix[i][j]=="1" else 0
            print(dp[i])
                # print(i,j,res)
        return res*res