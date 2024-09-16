#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 16:29
# @Author  : sunaolin
# @File    : 853.py

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        ps=[]
        for i in range(len(position)):
            ps.append((position[i],speed[i]))
        ps.sort()
        time=[]
        for v in ps:
            time.append(float(target-v[0])/float(v[1]))
        cnt=0
        i=len(time)-1
        while i>=0:
            head=time[i]
            while i>=0 and time[i]<=head:
                i-=1
            cnt+=1
        return cnt



