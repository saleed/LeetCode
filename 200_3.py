#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 10:32
# @Author  : sunaolin
# @File    : 200_3.py


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    res+=1
                    self.bfs(grid,i,j)
        return res



    def bfs(self,grid,i,j):

        vis=set()
        que=[(i,j)]
        vis.add((i,j))

        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while len(que)>0:
            head=que[0]
            que=que[1:]
            for s in range(4):
                ni=head[0]+dx[s]
                nj=head[1]+dy[s]
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and (ni,nj) not in vis and grid[ni][nj]=="1":
                    que.append((ni,nj))
                    vis.add((ni,nj))
                    grid[ni][nj]="0"





