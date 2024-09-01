#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 14:32
# @Author  : sunaolin
# @File    : 779.py


class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==1:
            return 0
        ret=self.kthGrammar(n-1,(k+1)//2)###因为k是从1开始，这里默认的k要从1开始
        if ret==1:
            if k%2==1:
                return 1
            else
                return 0
        else:
            if k%2==1:
                return 0
            else:
                return 1