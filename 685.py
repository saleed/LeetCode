#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 16:24
# @Author  : sunaolin
# @File    : 685.py


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        edict = {}
        for e in edges:
            if e[1] in edict:
                edict[e[1]].append(e[0])
            else:
                edict[e[1]] = [e[0]]

        while True:
            select = -1
            for node in edict:
                if len(edict[node])==0:
                    select = node
                    break
            if select == -1:
                break
            for k in edict:
                if select in edict[k]:
                    edict[k].remove(select)


        for k in edict:
            if len(edict[k])>1:
                return [edict[k][1],k]


        for v in edges[::-1]:
            if (v[0] in edict and v[1] in edict[v[0]]) or (v[1] in edict and v[0] in edict[v[1]]):
                return v


















