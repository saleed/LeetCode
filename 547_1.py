#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 14:25
# @Author  : sunaolin
# @File    : 547_1.py



class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        vis=set()
        cnt=0
        for i in range(len(isConnected)):
            if i not in vis:
                self.bfs(i,isConnected,vis)
                cnt+=1
        return cnt




    def bfs(self,i,isConnected,vis):
        vis.add(i)
        que=[i]
        while len(que)>0:
            head=que[0]
            que=que[1:]
            for j in range(len(isConnected[head])):
                if isConnected[head][j]==1 and j not in vis:
                    vis.add(j)
                    que.append(j)



