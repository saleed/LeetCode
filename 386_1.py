#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 15:49
# @Author  : sunaolin
# @File    : 386_1.py

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        self.dfs("",n,res)
        return res



    def dfs(self,tmp,n,res):
        if tmp>n:
            return
        res.append(str(tmp))
        for i in range(10):
            if i==0 and len(tmp)==0:
                continue
            tmp=tmp*10+i
            self.dfs(tmp,n,res)
            tmp=int(tmp/10)

