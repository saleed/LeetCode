#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 16:02
# @Author  : sunaolin
# @File    : 821.py

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """

        pos=[]
        for i in range(len(s)):
            if s[i]==c:
                pos.append(i)


        pos=[-float("inf")]+pos+[float("inf")]


        i=0
        j=0
        res=[]
        while i<len(s):
            if pos[j]<i<=pos[j+1]:
                res.append(max(abs(i-pos[j]),abs(i-pos[j+1])))
                i+=1
            else:
                j+=1
        return res




