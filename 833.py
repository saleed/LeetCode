#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 14:37
# @Author  : sunaolin
# @File    : 833.py

class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        cps=list(s)
        for i in range(len(indices)):
            j=indices[i]
            # print(s[j:j+len(sources[i])])
            if len(cps[j])>2 or len(cps[j])==0:##之前有替换过
                continue
            if cps[j]!=s[j]:
                continue
            if "".join(cps[j:j+len(sources[i])])==sources[i]:
                cps[j]=targets[i]
                for j in range(j+1,j+len(sources[i])):
                    cps[j]=""
            print(cps)
        return "".join(cps)