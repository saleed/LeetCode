#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 18:44
# @Author  : sunaolin
# @File    : 498_1.py

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        x=1
        y=-1
        res=[]
        while x!=len(mat)-1 or y!=len(mat[0])-1:
            while x-1>=0 and y+1<len(mat[0]):
                x-=1
                y+=1
                res.append(mat[x][y])
            if y<len(mat[0])-1:
                y+=1
            elif x<len(mat)-1:
                x+=1
            else:
                continue
            res.append(mat[x][y])

            while x+1<len(mat) and y-1>=0:
                x+=1
                y-=1
                res.append(mat[x][y])
            if x<len(mat)-1:
                x+=1
            elif y<len(mat[0])-1:
                y+=1
            else:
                continue
            res.append(mat[x][y])
        return res



