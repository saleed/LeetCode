#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 13:24
# @Author  : sunaolin
# @File    : 56_5.py


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        res=[]
        for v in intervals:
            if len(res)==0:
                res.append(v)
            else:
                if v[0]>res[-1][1]:
                    res.append(v)
                else:
                    res[-1][1]=max(res[-1][1],v[1])
        return res