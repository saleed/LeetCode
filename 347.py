#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 20:03
# @Author  : sunaolin
# @File    : 347.py

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        vdict={}
        for v in nums:
            if v in vdict:
                vdict[v]+=1
            else:
                vdict[v]=1
        # print(vdict)
        fdict={}
        for k in vdict:
            fdict[vdict[k]]=k
        print(vdict)
        keys=fdict.keys()
        keys.sort()
        # print(keys)
        res=[]
        for i in range(k):
            # print(keys[len(keys)-i])#######
            res.append(fdict[keys[len(keys)-i]]) #####i写成k
        return res


