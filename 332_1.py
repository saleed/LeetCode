#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 14:19
# @Author  : sunaolin
# @File    : 332_1.py

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        gph = {}
        for v in tickets:
            if v[0] not in gph:
                gph[v[0]] = [v[1]]
            else:
                gph[v[0]].append(v[1])
        for k in gph:
            gph[k].sort()
        # print(gph)
        # print(vis)
        res=[None]
        self.dfs("JPK",gph,len(tickets),[],res)
        return res[0]


    def dfs(self,start,gp,n,tmp,res):
        if n==0:
            res[0]=tmp[:]
            return True
        if start not in gp:
            return False
        dst=gp[start][:]
        for d in dst:
            gp[start].remove(d)
            tmp.append(d)
            if self.dfs(d,gp,n-1,tmp,res):
                return True
            tmp.pop()
            gp[start].append(d)
        return False





