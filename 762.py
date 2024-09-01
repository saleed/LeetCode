#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 14:24
# @Author  : sunaolin
# @File    : 762.py


class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        n=0
        while pow(2,n)-1<right:
            n+=1
        prime=self.getPrime(n)
        res=0
        for v in range(left,right+1):
            sumbit=0
            while v:
                sumbit+=v%10
                v/=10
            if sumbit in prime:
                res+=1
        return res



    def getPrime(self,n):
        prime=[1]*(n+1)
        for i in range(2,len(prime)):
            j=2
            while j*i<len(prime):
                prime[j*i]=0
                j+=1
        res=[]
        for i in range(2,len(prime)):
            if prime[i]==1:
                res.append(i)
        return res

