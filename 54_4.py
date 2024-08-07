#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 12:12
# @Author  : sunaolin
# @File    : 54_.py


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        vis=set()
        i=0
        j=-1
        res=[]
        while len(vis)!=len(matrix)*len(matrix[0]):
            while j+1<len(matrix[0]) and (i,j+1) not in vis:
                #####j += 1  ##这里先加了
                vis.add((i,j+1))
                res.append(matrix[i][j+1])
                j += 1  ##这里
            while i+1<len(matrix) and (i+1,j) not in vis:

                vis.add((i+1,j))
                res.append(matrix[i+1][j])
                i+=1
            while j-1>=0 and (i,j-1) not in vis:

                vis.add((i,j-1))
                res.append(matrix[i][j-1])
                j -= 1
            while i-1 >=0 and (i-1, j) not in vis:

                vis.add((i-1, j))
                res.append(matrix[i-1][j])
                i -= 1

        return res
