#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 16:31
# @Author  : sunaolin
# @File    : 424_1.py

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict={}
        tail=0
        maxl=0
        sumv=0
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
            maxv=max(dict.values())
            sumv+=1
            while sumv-maxv>k:
                sumv-=1
                dict[s[tail]]-=1
                tail+=1
                maxv=max(dict.values())
            maxl=max(maxl,i-tail+1)
        return maxl

