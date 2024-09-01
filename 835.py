#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 16:08
# @Author  : sunaolin
# @File    : 835.py


class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        one1=[]
        one2=[]
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j]==1:
                    one1.append((i,j))

        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1:
                    one2.append((i, j))

        offset={}
        for v1 in one1:
            for v2 in one2:
                k=(v1[0]-v2[0],v1[1]-v2[1])
                if k in offset:
                    offset[k]+=1
                else:
                    offset[k]=1

        maxv=0
        for k in offset:
            if maxv<offset[k]:
                maxv=offset[k]
        return maxv






