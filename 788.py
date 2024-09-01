#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 14:29
# @Author  : sunaolin
# @File    : 788.py



class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
##数学的方法
        dlist=[]
        while n:
            dlist.append(n%10)
            n/=10
        dlist=dlist[::-1]
        print(dlist)

        i=0
        res=0
        while i<len(dlist):
            prefix=dlist[:i]
            for j in range(dlist[i]):
                tmpprefix=prefix+[j]
                if tmpprefix[0]==0:
                    continue
                if 2 in tmpprefix or 5 in tmpprefix or 6 in tmpprefix or 9 in tmpprefix:
                    res+=pow(7,len(dlist)-i-1)
                else:
                    res+=pow(7,len(dlist)-i-1)-pow(3,len(dlist)-i-1)
            i+=1
        return res



