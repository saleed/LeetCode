#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 15:46
# @Author  : sunaolin
# @File    : 441_1.py

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0

        count=0
        r=1
        while count<n:
            count+=r
            r+=1

        return r-2



