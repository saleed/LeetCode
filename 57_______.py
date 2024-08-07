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
        i=0
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
        if i==len(intervals):
            return res
        res.append([min(res[i][0],newInterval[0]),max(res[i][1],newInterval[1])])
        i+=1
        while i<len(intervals) and intervals[i][0]<=res[-1][1]:
            res[-1][1]=max(intervals[i][1],res[-1][1])
            i+=1
        a=""
        a.tri
        return res

