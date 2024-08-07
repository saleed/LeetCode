#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 17:04
# @Author  : sunaolin
# @File    : 174_5.py

#每个点可累积的最大血量 如果最大血量大于0，
#每个点拥有


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        aggmax=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        minblood=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                if i==0 and j==0:
                    aggmax[i][j]=dungeon[i][j]
                    if aggmax[i][j]<0:
                        minblood[i][j]=aggmax[i][j]
                elif i==0:
                    aggmax[i][j]=aggmax[i][j-1]+dungeon[i][j]
                    minblood[i][j] = min(minblood[i][j-1],aggmax[i][j])

                elif j==0:
                    aggmax[i][j]=aggmax[i-1][j]+dungeon[i][j]
                    minblood[i][j] = min(minblood[i-1][j], aggmax[i][j])
                else:
                    aggmax[i][j]=max(aggmax[i][j-1],aggmax[i-1][j])+dungeon[i][j]
                    minblood[i][j] =max(min(aggmax[i][j-1]+dungeon[i][j],minblood[i][j-1]),min(aggmax[i-1][j]+dungeon[i][j],minblood[i-1][j]))
        return -minblood[-1][-1]+1

