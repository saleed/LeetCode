#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 21:55
# @Author  : sunaolin
# @File    : 692_1.py

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wdict={}
        for v in words:
            if v in wdict:
                wdict[v]+=1
            else:
                wdict[v]=1

        d=[]

        ##默认是最小堆，key默认为tuple[0],可以翻转key的正负号变成最大堆
        for s in wdict:
            heapq.heappush(d,(-wdict[s],s))
        res=[]
        while len(res)<k:
            res.append(heapq.heappop(d)[1])
        return res






