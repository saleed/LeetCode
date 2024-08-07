#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 17:15
# @Author  : sunaolin
# @File    : 409_1.py

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdict={}
        for v in s:
            if v in sdict:
                sdict[v]+=1
            else:
                sdict[v]=1
        flag=0
        res=0
        for k in sdict:
            if sdict[k]%2==0:
                res+=sdict[k]
            else:
                flag = 1
                res+=sdict[k]-1
        return res+flag

