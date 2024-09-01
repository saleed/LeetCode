#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 15:57
# @Author  : sunaolin
# @File    : 752.py

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        order=[]
        tmp=[i+1 for i in range(4)]
        self.permutation(4,0,tmp,order)

        for  od in order:
            tmp="0"*4
            flag=1
            for i in range(len(od)):
                if tmp in deadends:
                    flag=0
                    break
                else:
                    l=min(tmp[i],od[i])
                    r=max(tmp[i],od[i])



    def permutation(self,n,i,tmp,res):
        if i==n:
            res.append(tmp[:])
            return
        for j in range(i+1,n):
            tmp[j],tmp[i]=tmp[i],tmp[j]
            self.permutation(n,i+1,tmp,res)
            tmp[j],tmp[i]=tmp[i],tmp[j]




