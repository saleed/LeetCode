#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 14:01
# @Author  : sunaolin
# @File    : 254_1.py


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.dfs(n,2)



    ##核心是怎么保证结果不重复
    def dfs(self,n,l):
        res=[]
        for i in range(l,int(math.sqrt(n))+1):
            if n%i==0:
                res.append([n//i,i])
                for v in self.dfs(n//i,i):
                    res.append(v+[i])
        return res
