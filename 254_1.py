#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 14:01
# @Author  : sunaolin
# @File    : 254_1.py


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        sq=math.sqrt(n)
        res=[]
        for i in range(2,sq+1):
            while n%i==0:
                res.append(i)
        return res
