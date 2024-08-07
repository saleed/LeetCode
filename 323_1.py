#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 17:50
# @Author  : sunaolin
# @File    : 323_1.py

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph={}
        for v in edges:
            if v[0] in graph:
                graph[v[0]].append(v[1])
            else:
                graph[v[1]]=[v[0]]

            if v[1] in graph:
                graph[v[1]].append(v[0])
            else:
                graph[v[0]]=[v[1]]
        vis=set()
        ret=0
        for i in range(n):
            if i not in vis and i in graph:
                self.dfs(graph,i,vis)
                ret+=1
        return ret


    def dfs(self,graph,i,vis):

        for v in graph[i]:
            if v not in vis:
                vis.add(i)
                self.dfs(graph,v,vis)

