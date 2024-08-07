#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 14:20
# @Author  : sunaolin
# @File    : 59_5.py


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        i=0
        j=-1
        res=[[0 for _ in range(n)] for _ in range(n)]
        num=0
        while num<n*n:
            while j+1<n and res[i][j+1]==0:
                j+=1
                res[i][j] = num + 1
                num+=1
            while i+1<n and res[i+1][j]==0:
                i+=1
                res[i][j] = num + 1
                num+=1
            while i-1>=0 and res[i-1][j]==0:
                i-=1
                res[i][j] = num + 1
                num+=1
            while j-1>=0 and res[i][j-1]==0:
                j-=1
                res[i][j]=num+1
                num+=1
        return res
