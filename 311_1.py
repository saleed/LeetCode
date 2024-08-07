#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 13:35
# @Author  : sunaolin
# @File    : 311_1.py


class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """

        res=[[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                sumv=0
                for k in range(len(mat1[0])):
                    sumv+=mat1[i][k]*mat2[k][j]
                res[i][j]=sumv
        return res


        #
        #
        #
        #
        # m1={}
        # m2={}
        # for i in range(len(mat1)):
        #     m1[i]={}
        #     for j in range(len(mat1[0])):
        #         m1[i][j]=mat1[i][j]
        #
        # for i in range(len(mat2[0])):
        #     m2[i]={}
        #     for j in range(len(mat2)):
        #         m2[i][j]=mat2[i][j]
        #
        #
        # for i in range(len(mat1)):
        #     for j in range(len(mat2[0])):
        #         sumv=0
        #         for k in range(len(mat1[0])):
        #             sumv+=mat1[i][k]*mat2[]
        #
        #
        #
        #
