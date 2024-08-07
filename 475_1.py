#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/24 17:27
# @Author  : sunaolin
# @File    : 475_1.py


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()
        i=0
        j=0
        minr=0


        ##可以证明，d2的距离小于d1的情况
        while i<len(houses):
            d1=abs(heaters[j]-houses[i])
            d2=float('inf') if j+1>=len(heaters) else abs(heaters[j+1]-houses[i])
            if d2<=d1: ###<的情况是错的，小于等于直接更新j
                j+=1
                continue
            if i:
                print(i,j,d1,d2)
            minr=max(minr,d1)
            i+=1
        return minr


