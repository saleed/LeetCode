#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 14:39
# @Author  : sunaolin
# @File    : 313_3.py


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n==1:
            return 1
        ptr=[0]*len(primes)
        i=0
        res=[1]
        while len(res)<n:
            sel=-1
            minv=float("inf")
            for i in range(len(primes)):
                if res[ptr[i]]*primes[i]<=minv:
                    minv=res[ptr[i]]*primes[i]
                    sel=i
            ptr[sel]+=1
            print(res)
            if minv==res[-1]:
                continue
            res.append(minv)
        return res[-1]