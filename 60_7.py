#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 14:31
# @Author  : sunaolin
# @File    : 60_7.py


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel=[str(i+1) for i in range(n)]
        res=""
        # k=k-1
        i=n-1
        while i>=0:
            fac=self.fac(i)
            div=int(max(0,(k-1))/fac)  ####注意这里，这里k有可能为0，导致k-1<0
            print("fac",fac,k-1,div,sel)
            res+=str(sel[div])
            k-=(div*fac)
            sel.remove(sel[div])
            # break
            i-=1
        return res



    def fac(self,n):
        if n<=1:
            return 1
        else:
            res=1
            for i in range(n):
                res*=(i+1)
            return res