#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 15:34
# @Author  : sunaolin
# @File    : 750.py



class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        for i in range(len(grid)):
            for j in range(i):
                bitand=self.bitAnd(grid[i],grid[j])
                sumv=sum(bitand)
                if sumv>2:
                    res+=sumv*(sumv-1)/2
        return res



    def bitAnd(self,l1,l2):
        res=[]
        for i in range(len(l1)):
            res.append(l1[i]&l2[i])
        return res






