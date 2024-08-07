#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 11:25
# @Author  : sunaolin
# @File    : 605_1.py

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt=0
        i=0
        while i<len(flowerbed):
            if flowerbed[i]==0 and ((i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0)):
                flowerbed[i]=1
                cnt+=1
            if cnt>=n:
                return True
            i+=1
        return False

