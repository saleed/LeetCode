#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 18:11
# @Author  : sunaolin
# @File    : 74_4.py


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
        j=len(matrix)-1
        while i<len(matrix) and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                j+=1
            else:
                i-=1
        return False