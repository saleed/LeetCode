#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/30 17:06
# @Author  : sunaolin
# @File    : 845.py

class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        lasc=[0]*len(arr)
        rasc=[0]*len(arr)

        for i in range(len(arr)):
            if i==0 or arr[i]<arr[i-1]:
                lasc[i]=1
            else:
                lasc[i]=lasc[i-1]+1

        maxl=0
        for i in range(len(arr))[::-1]:
            if i==len(arr)-1 or arr[i]<arr[i+1]:
                rasc[i]=1
            else:
                rasc[i]=rasc[i+1]+1
            maxl=max(maxl,lasc[i]+rasc[i]-1)
        return maxl








