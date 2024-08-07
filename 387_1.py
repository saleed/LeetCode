#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 16:02
# @Author  : sunaolin
# @File    : 387_1.py


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        vdict={}
        for v in s:
            if v in vdict:
                vdict[v]+=1
            else:
                vdict[v]=1

        for i in range(len(s)):
            if vdict[s[i]]==1:
                return i
        return -1

