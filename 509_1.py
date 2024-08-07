#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 14:21
# @Author  : sunaolin
# @File    : 509_1.py

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        p=1
        q=0
        nx=0
        for i in range(2,n+1):
            nx=p+q
            q=p
            p=nx

        return nx


a=Solution()
print(a.fib(3))