#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 14:20
# @Author  : sunaolin
# @File    : 436.py


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        idict={} ##记录sort后的位置

        pdict={} ##记录位置

        for i in range(len(intervals)):
            pdict[(intervals[i][0],intervals[i][1])] = i

        sortitv=intervals[:]
        sortitv.sort()
        for i in range(len(intervals)):
            idict[(sortitv[i][0],sortitv[i][1])] = i
        res=[]

        for v in intervals:

            id=idict[tuple(v)]
            while id<len(sortitv) and sortitv[id][0]<v[1]:
                id+=1
            if id==len(sortitv):
                res.append(-1)
            else:
                res.append(pdict[(sortitv[id][0],sortitv[id][1])])
        return res



