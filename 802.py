#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 10:50
# @Author  : sunaolin
# @File    : 802.py


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        res=[]
        while True:
            find=-1
            for i  in range(len(graph)):
                if len(graph[i])==0 and i not in res:
                    find=i
                    break
            if find:
                res.append(find)
            else:
                break
            for i in range(len(graph)):
                graph[i].remove(find)
        res.sort()
        return res


