#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 10:57
# @Author  : sunaolin
# @File    : 210_3.py


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        Gadj={}
        for i in range(numCourses):
            Gadj[i]=[]
        for v in prerequisites:
            Gadj[v[0]].append(v[1])

        res=[]
        while len(Gadj.keys())>0:
            delV=-1
            for k in Gadj.keys():
                if len(Gadj[k])==0:
                    delV=k
                    break
            if delV==-1:
                return []
            del Gadj[delV]

            for k in Gadj.keys():
                if delV in Gadj[k]:
                    Gadj[k].remove(delV)

            res.append(delV)
        return res




