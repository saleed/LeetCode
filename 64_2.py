#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 16:00
# @Author  : sunaolin
# @File    : 64_2.py


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.bfs(grid)

    def bfs(self, grid):
        # mindist = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        mindist={}
        mindist[(0,0)]= grid[0][0]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        que = [(0, 0)]
        while len(que) > 0:
            tmp = que[0]
            que = que[1:]
            x = tmp[0]
            y = tmp[1]

            for i in range(4):
                nx = x+ dx[i]
                ny = y + dy[i]
                if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and \
                        ((nx, ny) not in mindist or mindist[(nx, ny)] > mindist[(x, y)] + grid[nx][ny]):
                    que.append((nx, ny))
                    mindist[(nx, ny)] = mindist[(x, y)] + grid[nx][ny]
        print(mindist)
        return mindist[(len(grid)-1,len(grid[0])-1)]






