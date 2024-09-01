#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 15:09
# @Author  : sunaolin
# @File    : 767.py



class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        ndict={}
        for v in s:
            if v in ndict:
                ndict[v]+=1
            else:
                ndict[v]=1
        nlist=[]
        for k in ndict:
            nlist.append((-ndict[k],k))

        for v in ndict.values():
            if v>(len(s)+1)/2:
                return ""

        res=""
        while len(res)<len(s):
            tmp=heapq.pop(nlist)
            res+=tmp[1]
            if tmp[0]>1:
                heapq.heappush((tmp[0]-1,tmp[1]))
        return res