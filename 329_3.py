#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 10:50
# @Author  : sunaolin
# @File    : 329_3.py


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        mt=[(i,j,matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[0]))]

        mt.sort(key=lambda x:x[2])


        dist=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        maxl=0
        for i in range(len(mt)):
            for j in range(4):
                x=mt[i][0]
                y=mt[i][1]
                nx=x+dx[j]
                ny=y+dy[j]
                if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and mt[i][2]<matrix[nx][ny]:
                    dist[nx][ny]=max(dist[nx][ny],dist[x][y]+1)
                    maxl=max(maxl,dist[nx][ny])

        return maxl



