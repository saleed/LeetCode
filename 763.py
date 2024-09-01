#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 14:38
# @Author  : sunaolin
# @File    : 763.py



class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        bound={}

        for i in range(len(s)):
            if s[i] in bound:
                bound[s[i]][1]=i
            else:
                bound[s[i]]=[i,i]

        i=0
        res=[]
        while i<len(s):
            end=bound[s[i]][1]
            print(i,end)
            j=i
            while j<end:
                if bound[s[j]][1]>end:
                    end=bound[s[j]][1]
                j+=1
            res.append(end-i+1)
            i=end+1
        return res

            