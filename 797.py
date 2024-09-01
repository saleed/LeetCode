#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 19:33
# @Author  : sunaolin
# @File    : 797.py


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(graph,res,[0],0,len(graph)-1)
        return res


    def dfs(self,graph,res,path,tmpv,n):
        if tmpv==n:
            res.append(path[:])
        for v in graph[tmpv]:
            self.dfs(graph,res,path+[v],v,n)

