#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 21:13
# @Author  : sunaolin
# @File    : 463_1.py

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        vis=set()
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in vis:
                    res+=self.bfs(grid,i,j,vis)

        return  res

    def bfs(self,grid,x,y,vis):
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        que=[(x,y)]
        vis.add((x,y))
        res=0
        while len(que)>0:
            head=que[0]
            que=que[1:]
            for i in range(4):
                nx=head[0]+dx[i]
                ny=head[1]+dy[i]
                if (nx,ny) in vis:
                    continue

                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                    que.append((nx,ny))
                    print((nx,ny))
                    vis.add((nx,ny))
                else:
                    res+=1
        return res

