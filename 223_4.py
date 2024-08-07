#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 17:13
# @Author  : sunaolin
# @File    : 223_4.py

class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        areaa=(ay2-ay1)*(ax2-ax1)
        areab=(by2-by1)*(bx2-bx1)

        if ax2<=bx1 or bx2<=ax1 or ay2<=by1 or by2<=ay1:
            return areab+areaa
        x=min(ax2,bx2)-max(ax1,bx1)
        y=min(ay2,by2)-max(ay1,by1)
        return areab+areaa-x*y