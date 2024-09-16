#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 15:20
# @Author  : sunaolin
# @File    : 851.py


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """

        g={}
        for i in range(len(quiet)):
            g[i]=[]
        for v in richer:
            g[v[1]].append(v[0])
        answer=[float("inf")]*len(quiet)
        for i in range(len(quiet)):
            self.dfs(g,quiet,i,answer)
        return answer




        ##使用深度优先搜索，当前节点的最小安静值，一定是当前节点或邻居节点中安静值最小的一个
    def dfs(self,g,quiet,k,answer):
        if answer[k]!=float("inf"):
            return answer[k]

        answer[k]=quiet[k]
        if len(g[k])!=0:
            for i in g[k]:
                answer[k]=min(answer[k],self.dfs(g,quiet,i,answer))
        return answer[k]






