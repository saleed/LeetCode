#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 13:56
# @Author  : sunaolin
# @File    : 267_1.py


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cdict={}
        for v in s:
            if v in cdict:
                cdict[v]+=1
            else:
                cdict[v]=1
        singleN=[]
        for k in cdict:
            if cdict[k]%2!=0:
                singleN.append(k)
        if len(singleN)>1:
            return []
        tmp=""
        if len(singleN)==1:
            tmp=singleN[0]
            cdict[tmp]-=1
            if cdict[tmp]==0:
                del cdict[tmp]

        res=[]
        self.dfs(cdict,tmp,res)
        return res

    def dfs(self,cdict,tmp,res):
        if len(cdict)==0:
            res.append(tmp[:])
            return
        keys=cdict.keys()
        for k in keys:
            cdict[k]-=2
            if cdict[k]==0:
                del cdict[k]
            tmp=k+tmp+k
            self.dfs(cdict,tmp,res)
            tmp=tmp[1:-1]
            if k not in cdict:
                cdict[k]=2
            else:
                cdict[k]+=2




