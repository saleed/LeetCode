#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 13:26
# @Author  : sunaolin
# @File    : 57_5.py

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        if len(intervals)==0:
            return [newInterval]

        i=0
        while i<len(intervals):
            tmp=intervals[i]
            if tmp[1]<newInterval[0]:
                res.append(tmp)
            else:
                break
            i+=1
        if i<len(intervals):
            if intervals[i][1]<intervals[i][0]:
                res.append(newInterval)
                res.append(intervals[i])
            else:
                res.append([min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])])
        else:
            res.append(newInterval)
        i+=1
        while i<len(intervals):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            elif intervals[i][0]<=res[-1][1]:
                res[-1][1]=max(intervals[i][1],res[-1][1])
            i+=1
        return res
