#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 13:19
# @Author  : sunaolin
# @File    : 609_1.py


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        pdcit={}
        for v in paths:
            p=v.split(" ")
            base=p[0]

            for f in p[1:]:
                i=0
                while i<len(f) and f[i]!="(":
                    i+=1
                ct=f[i+1:-1]
                if ct not in pdcit:
                    pdcit[ct]=[base+"/"+f[:i]]
                else:
                    pdcit[ct].append(base + "/" + f[:i])
        res=[]
        for k in pdcit:
            if len(pdcit[k])>=2:
                res.append(pdcit[k])

        return res