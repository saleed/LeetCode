#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 22:04
# @Author  : sunaolin
# @File    : 785.py


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        vis=dict()

        for i in range(len(graph)):
            if i not in vis:

                if not self.dfs(graph,vis,i):
                    print(i)
                    return False
                # print(vis)
        return True




    def dfs(self,graph,vis,tmpn):
        print(vis)
        preclr=vis[tmpn]
        for v in graph[tmpn]:
            if v in vis:
                if preclr==vis[v]:
                    return False
                else:
                    continue
            vis[v]=not preclr
            if self.dfs(graph,vis,v):

            del vis[v]





