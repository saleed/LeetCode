#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/20 15:40
# @Author  : sunaolin
# @File    : 60_8.py

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel=[i+1 for i in range(n)]
        res=""
        k=k-1
        for i in range(n):
            id=int((k)/self.fac(n-1-i))
            res+=str(sel[id])
            sel.remove(sel[id])
            k=k%self.fac(n-1-i)
            print(id,k)
        return res

    def fac(self,n):
        if n<=1:
            return 1
        else:
            res=1
            for i in range(n):
                res*=(i+1)
            return res