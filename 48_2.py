#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/19 21:07
# @Author  : sunaolin
# @File    : 48-2.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 18:18
# @Author  : sunaolin
# @File    : 48.py

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """


        for i  in range(len(matrix)/2):
            for j in range(i,len(matrix)-1-i):
                tmp=matrix[i][j]
                matrix[i][j]=matrix[len(matrix)-1-j][i]
                matrix[len(matrix)-1-j][i]=matrix[len(matrix) - 1 -i][len(matrix)-1-j]
                matrix[len(matrix) - 1 -i][len(matrix)-1-j]=matrix[j][len(matrix)-1-i]
                matrix[j][len(matrix)-1-i]=tmp
        return matrix

