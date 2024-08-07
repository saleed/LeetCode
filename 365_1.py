#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 16:14
# @Author  : sunaolin
# @File    : 365_1.py


class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        vis=set()
        return self.dfs(jug1Capacity,jug2Capacity,0,0,vis,targetCapacity)


    def dfs(self,x,y,xv,yv,vis,target):
        # print(xv,yv)
        if (xv,yv) in vis:
            return False
        if xv==target or yv==target or xv+yv==target:
            return True
        vis.add((xv,yv))
        res1=self.dfs(x,y,x,yv,vis,target)
        if res1:
            return True
        res2=self.dfs(x,y,xv,y,vis,target)
        if res2:
            return True
        res3=self.dfs(x,y,min(xv+yv,x),max(0,yv-(x-xv)),vis,target)
        if res3:
            return True
        res4=self.dfs(x,y,max(0,xv-(y-yv)),min(xv+yv,y),vis,target)
        if res4:
            return True
        res5=self.dfs(x,y,0,yv,vis,target)
        if res5:
            return True
        res6=self.dfs(x,y,xv,0,vis,target)
        if res6:
            return True
        return False






