#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/6 14:45
# @Author  : sunaolin
# @File    : 651_1.py


class Solution(object):
    def maxA(self, n):
        """
        :type n: int
        :rtype: int
        """
        best=[0]*(n+1)
        best[1]=1
        for i in range(2,n+1):
            best[i]=best[i-1]+1
            for j in range(i):
                if i-j-3>=0:
                    best[i]=max(best[i],best[j]*(i-j-2))
        print(best)

        return best[-1]

