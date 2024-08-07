#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 15:54
# @Author  : sunaolin
# @File    : 624_1.py

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        maxitv=[arrays[0][0],arrays[0][-1]]
        maxdiff=0
        for v in arrays:
            maxdiff=max(maxdiff,abs(maxitv[0]-v[-1]),abs(maxitv[1]-v[0]))
            maxitv[0]=min(maxitv[0],v[0])
            maxitv[1]=max(maxitv[1],v[-1])
        return maxdiff
