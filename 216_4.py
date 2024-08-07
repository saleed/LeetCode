#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 14:49
# @Author  : sunaolin
# @File    : 216——4.py


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(k,n,1,[],res)
        return res


    def dfs(self,k,n,i,tmp,res):
        if n==0 and k==0:
            res.append(tmp[:])
            return
        if k>0 and i<10:
            self.dfs(k,n,i+1,tmp,res)
            tmp.append(i)
            self.dfs(k-1,n-i,i+1,tmp,res)
            tmp.pop()


