#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 20:34
# @Author  : sunaolin
# @File    : 174——4.py

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        ###记录到达最后一个点时候需要的最少血量
        blood=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        ##从最后一个点遍历

        for i in range(len(dungeon))[::-1]:
            for j in range(len(dungeon[0]))[::-1]:
                if i==len(dungeon)-1 and j==len(dungeon[0])-1:
                    blood[i][j]=max(0,-dungeon[i][j])
                elif i==len(dungeon)-1:
                    blood[i][j]=max(0,blood[i][j+1]-dungeon[i][j])
                elif j==len(dungeon[0])-1:
                    blood[i][j] = max(0, blood[i+1][j] - dungeon[i][j])
                else:
                    # print(i,j)
                    blood[i][j]=min(max(0, blood[i+1][j] - dungeon[i][j]),max(0,blood[i][j+1]-dungeon[i][j]))
            print(blood[i])
        return blood[0][0]+1