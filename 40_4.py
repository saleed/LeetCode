#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 20:55
# @Author  : sunaolin
# @File    : 40_4.py


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candi={}
        for v in candidates:
            if v in candi:
                candi[v]+=1
            else:
                candi[v]=1

        keys=candi.keys()
        res=[]
        self.dfs2(candi,target,keys,0,[],res)
        # res=[]
        # self.dfs(candidates,target,0,[],res)
        return res




    ##会导致重复
    def dfs(self,candi,target,i,tmp,res):
        if i==len(candi) and target==0:
            res.append(tmp[:])
            return
        if i<len(candi) and target>=0:
            self.dfs(candi,target,i+1,tmp,res)
            tmp.append(candi[i])
            self.dfs(candi,target,target-candi[i],tmp,res)
            tmp.pop()

    ###构造字典 这里candi是个

    def dfs2(self,candi,target,keys,i,tmp,res):
        if i==len(keys) and target==0:
            res.append(tmp[:])
            return
        if i<len(keys):
            n=0
            while n<=candi[i] and n*candi[i]<=target:
                newtmp=tmp[:]
                newtmp.extend([candi[i]]*n)
                self.dfs2(candi,target,keys,i+1,newtmp,res)
                n+=1




