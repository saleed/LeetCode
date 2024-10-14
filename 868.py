#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 15:55
# @Author  : sunaolin
# @File    : 868.py


class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxl=0
        l=-float("inf")
        while n:
            left=n%2
            if left==0:
                l+=1
            else:
                maxl=max(maxl,l)
                l=0
            n/=2
        return maxl+1 if maxl!=0 else 0