#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 13:31
# @Author  : sunaolin
# @File    : 484_1.py

class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[i for i in range(1,len(s)+1)]


        j=0
        i=0
        while j<len(s):
            if s[j]=="D":
                i=j
                while s[j]=="D":
                    j+=1
                p=i
                q=j
                while p<q:
                    res[p],res[q]=res[q],res[p]
                    p+=1
                    q-=1
            else:
                j+=1
        return res




