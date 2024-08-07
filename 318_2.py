#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 16:50
# @Author  : sunaolin
# @File    : 318_2.py


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bdict={}
        for v in words:
            k=0
            for s in list(set(v)):
                k+=(1<<(ord(s)-ord('a')))
            if k in bdict:
                bdict[k]=max(bdict[k],len(v))
            else:
                bdict[k]=len(v)

        res=0
        for k1 in bdict:
            for k2 in bdict:
                if k1&k2>0:
                    continue
                else:
                    res=max(res,bdict[k1]*bdict[k2])
        return res
