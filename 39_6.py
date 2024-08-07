#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 20:24
# @Author  : sunaolin
# @File    : 39_6.py


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(candidates,0,target,[],res)
        return res


    def dfs(self,candi,i,target,tmp,res):
        if i==len(candi):
            res.append(tmp[:])
            return
        n=0
        while n*candi[i]<target:
            tmp.extend(candi[i]*n)
            self.dfs(candi,i+1,target-n*candi[i],tmp,res)
            if n>0:
                tmp=tmp[:-n]




a=[1,3,2]
print(a[:-1])

