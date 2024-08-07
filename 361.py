#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 15:24
# @Author  : sunaolin
# @File    : 361.py

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        down=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        up=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        left=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        right=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="E":
                    down[i][j]=1 if i==0 else down[i-1][j]+1
                    left[i][j]=1 if j==0 else left[i][j-1]+1
                elif grid[i][j]=="W":
                    down[i][j]=0
                    left[i][j]=0
                else:
                    down[i][j]=0 if i==0 else down[i-1][j]
                    left[i][j]=0 if j==0 else left[i][j-1]

        for i in range(len(grid))[::-1]:
            for j in range(len(grid[0]))[::-1]:
                if grid[i][j] == "E":
                    up[i][j] = 1 if i == len(grid)-1 else up[i + 1][j] + 1
                    right[i][j] = 1 if j == len(grid[0])-1 else right[i][j + 1] + 1
                elif grid[i][j] == "W":
                    up[i][j] = 0
                    right[i][j] = 0
                else:
                    up[i][j] = 0if i == len(grid)-1  else up[i + 1][j]
                    right[i][j] = 0 if j == len(grid[0])-1 else right[i][j + 1]

        res=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="E":
                    res=max(res,left[i][j]+right[i][j]+up[i][j]+down[i][j]-3)
                elif grid[i][j]=="0":
                    res=max(res,left[i][j]+right[i][j]+up[i][j]+down[i][j])
        return res


