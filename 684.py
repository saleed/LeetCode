#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 15:55
# @Author  : sunaolin
# @File    : 684.py

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        edict={}

        for e in edges:
            if e[0] in edict:
                edict[e[0]].append(e[1])
            else:
                edict[e[0]]=[e[1]]

            if e[1] in edict:
                edict[e[1]].append(e[0])
            else:
                edict[e[1]]=[e[0]]

        while True:

            select=-1

            for node in edict:
                if len(edict[node])==1:
                    select=node
                    break
            if select==-1:
                break
            adj=edict[select][0]
            del edict[select]
            edict[adj].remove(select)

        for v in edges[::-1]:
            if (v[0] in edict and v[1] in edict[v[0]]) or (v[1] in edict and v[0] in edict[v[1]]):
                return v




