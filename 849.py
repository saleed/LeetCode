#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/31 16:27
# @Author  : sunaolin
# @File    : 849.py


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ret=-1
        maxnum=0
        i=0
        for i in range(len(seats)):
            if seats[i]==1:
                maxnum=max(maxnum,i)
                break
        for i in range(len(seats))[::-1]:
            if seats[i]==1:
                maxnum=max(maxnum,len(seats)-(i+1))
                break

        while i<len(seats):
            if seats[i]==1:
                i+=1
            else:
                start=i
                while i<len(seats) and seats[i]==0:
                    i+=1
                if (i-start/2):
                    maxnum=max(m,(i-1+start)/2)
        return ret
