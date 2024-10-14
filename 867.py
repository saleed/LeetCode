#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 15:36
# @Author  : sunaolin
# @File    : 867.py


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        tp=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tp[j][i]=matrix[i][j]
        return tp


