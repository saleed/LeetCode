#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 15:01
# @Author  : sunaolin
# @File    : 766.py


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """


        for j in range(len(matrix[0])):
            i=0
            base=matrix[i][j]
            while i<len(matrix) and j <len(matrix[0]):
                if matrix[i][j]!=base:
                    return False
                i+=1
                j+=1
        for i  in range(1,len(matrix)):
            j=0
            base = matrix[i][j]
            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != base:
                    return False
                i += 1
                j += 1

        return True
