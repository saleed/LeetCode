#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 18:25
# @Author  : sunaolin
# @File    : 812.py

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        maxarea=-float("inf")
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if i!=j and i!=k and j!=k:
                        maxarea=max(maxarea,self.triArea([points[i],points[j],points[k]]))
        return maxarea

    def triArea(self,ps):
        a=self.lenEdge(ps[0],ps[1])
        b=self.lenEdge(ps[0],ps[2])
        c=self.lenEdge(ps[1],ps[2])
        p=(a+b+c)/2

        return math.sqrt(p*(p-a)*(p-b)*(p-c))




    def lenEdge(self,p1,p2):
        return math.sqrt(pow((p1[0]-p2[0]),2)+pow(p1[1]-p2[1],2))