#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 19:49
# @Author  : sunaolin
# @File    : 799.py

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """

        i=1
        p=poured
        while p-i>=0:
            p-=i
            i+=1
        if query_row<(i-1):
            return 1

        if query_glass==0 or query_glass==i-1
            return p/(2*(i-1))
        else:
            return 2*p/(2*(i-1))

