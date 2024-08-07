#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 09:22
# @Author  : sunaolin
# @File    : 438_1.py

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        cdict={}
        for v in p:
            if v in cdict:
                cdict[v]+=1
            else:
                cdict[v]=1
        cp_cdict=copy.deepcopy(cdict)
        res=[]
        left=-1
        for i in range(len(s)):
            # print(i,cp_cdict)
            if s[i] in cp_cdict:
                cp_cdict[s[i]]-=1
                if i-len(p)>left and s[i-len(p)] in cp_cdict:
                    cp_cdict[s[i-len(p)]]+=1
                if self.checkEmpty(cp_cdict):
                    res.append(i-len(p)+1)
            else:
                left=i
                cp_cdict = copy.deepcopy(cdict)

        return res


    def checkEmpty(self,cdict):
        for k in cdict:
            if cdict[k]>0:
                return False
        return True

