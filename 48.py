#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 18:18
# @Author  : sunaolin
# @File    : 48.py
##重点关注
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=int(len(matrix)/2)
        for i in range(l+1):
            for j in range(i,len(matrix)-i-1):###注意这里是-i-1!!!!!!!
                print(i,j)

                tmp=matrix[i][j]
                print(tmp)
                matrix[i][j]=matrix[len(matrix)-1-j][i]
                matrix[len(matrix)-1-j][i]=matrix[len(matrix)-1-i][len(matrix)-1-j]
                matrix[len(matrix)-1-i][len(matrix)-1-j]=matrix[j][len(matrix)-1-i]
                matrix[j][len(matrix) - 1 - i]=tmp
        return matrix



