#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 19:41
# @Author  : sunaolin
# @File    : 90_4.py


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cdict={}
        for v in nums:
            if v in cdict:
                cdict[v]+=1
            else:
                cdict[v]=1
        res=[]
        self.dfs(cdict,cdict.keys(),0,[],res)
        return res


    def dfs(self,cdict,keys,i,tmp,res):
        if i==len(keys):
            res.append(tmp[:])
            return
        for n in range(cdict[keys[i]]+1):
            tmp.extend(n*[keys[i]])
            self.dfs(cdict,keys,i+1,tmp,res)
            tmp=tmp[:len(tmp)-n]
