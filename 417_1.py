#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 12:00
# @Author  : sunaolin
# @File    : 417_1.py

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ##reach表示之前已经算出可以抵达大西洋和太平洋的节点
        ##dfs从height 从小到大遍历，算出的结果存储于reach避免重复计算

        h=[]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                h.append((i,j,heights[i][j]))
        h.sort(key=lambda x:x[2])
        reach=[[-1 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        res=[]
        for v in h:
            vis=set()
            vis.add((v[0],v[1]))
            if self.dfs(heights,v[0],v[1],reach,vis)==3:
                res.append(v[:-1])
            vis.remove((v[0], v[1]))
        for v in reach:
            print(v)
        return res


    def dfs(self,heights,x,y,reach,vis):
        print(x,y,len(reach),len(reach[0]))
        if 0<=x<len(reach) and 0<=y<len(reach[0]) and reach[x][y]!=-1:
            return reach[x][y]
        ####分别用0，1，2,3编码不可到达，，可到达太平洋，可到达大西洋 都可到达三种情况
        if x==-1 or y==-1:
            return 1
        if x==len(heights) or y==len(heights[0]):
            return 2
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        res=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx==-1 or ny==-1 or nx==len(heights) or ny==len(heights[0])) \
                    or (0<=nx<len(heights) and 0<=ny<len(heights[0])
                        and heights[nx][ny]<=heights[x][y]) and (nx,ny) not in vis:
               vis.add((nx,ny))
               ret=self.dfs(heights,nx,ny,reach,vis)
               vis.remove((nx, ny))
               if ret==3:
                   res=3
                   break
               else:
                   res=res|ret

        # print(x,y)
        reach[x][y]=res
        return res





