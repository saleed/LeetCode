#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 13:57
# @Author  : sunaolin
# @File    : 490_1.py


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        vis=set()
        vis.add((start[0],start[1]))
        return self.dfs(maze,vis,start[0],start[1],destination[0],destination[1])



    def dfs(self,maze,vis,xs,ys,xe,ye):
        if xs==xe and ys==ye:
            return True
        x=xs
        y=ys
        while x+1<len(maze) and maze[x+1][y]==0:
            x+=1
        if (x,y) not in vis:
            vis.add((x,y))
            if self.dfs(maze,vis,x,y,xe,ye):
                return True
        x = xs
        y = ys
        while x-1>=0 and maze[x - 1][y] == 0:
            x-=1
        if (x, y) not in vis:
            vis.add((x, y))
            if self.dfs(maze, vis, x, y, xe, ye):
                return True

        x = xs
        y = ys
        while y+1 < len(maze[0]) and maze[x][y+1] == 0:
            y+=1
        if (x, y) not in vis:
            vis.add((x, y))
            if self.dfs(maze, vis, x, y, xe, ye):
                return True

        x = xs
        y = ys
        while y-1>=0 and maze[x][y-1] == 0:
            y-=1
        if (x, y) not in vis:
            vis.add((x, y))
            if self.dfs(maze, vis, x, y, xe, ye):
                return True
        return False




