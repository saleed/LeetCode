#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/22 18:16
# @Author  : sunaolin
# @File    : 73.py

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        zrow=set()
        zcol=set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zrow.add(i)
                    zcol.add(j)

        for r in zrow:
            for j in range(len(matrix[0])):
                matrix[r][j]=0
        for c in zcol:
            for i in range(len(matrix)):
                matrix[i][c]=0
