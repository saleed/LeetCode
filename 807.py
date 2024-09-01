#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 13:39
# @Author  : sunaolin
# @File    : 807.py

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        maxh=[[float("inf") for _ in range(len(grid))] for _ in range(len(grid))]

        n=len(grid)
        for i in range(n):
            h=0
            for j in range(n):
                h=max(grid[i][j],h)
            for j in range(n):
                maxh[i][j]=min(maxh[i][j],h)

        for j in range(n):
            h = 0
            for i in range(n):
                h = max(grid[i][j], h)
            for i in range(n):
                maxh[i][j] = min(maxh[i][j], h)


        res=0
        for i in range(n):
            for j in range(n):
                res+=maxh[i][j]-grid[i][j]
        return res







