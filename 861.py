#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/16 23:02
# @Author  : sunaolin
# @File    : 861.py

class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in range(len(grid)):
            if grid[i][0]==0:
                for j in range(len(grid[0])):
                    grid[i][j]=1 if grid[i][j]==0 else 0

        for j in range(len(grid[0])):
            cnt=0
            for i in range(len(grid)):
                if grid[i][j]==1:
                    cnt+=1
            if cnt<=len(grid)/2:
                for i in range(len(grid)):
                    grid[i][j]=1 if grid[i][j]==0 else 0

        res=0
        for i in range(len(grid)):
            tmp=0
            for j in range(len(grid)):
                tmp+=(tmp<<1)+grid[i][j]
            res+=tmp
        return res

