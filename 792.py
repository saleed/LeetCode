#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 17:25
# @Author  : sunaolin
# @File    : 792.py


class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """



        pos={}
        for i in range(len(s)):
            if s[i] in pos:
                pos[s[i]].append(i)
            else:
                pos[s[i]]=[i]

        res=[]
        for v in words:
            if len(v)>len(s):
                continue
            p=-1
            issub=True
            for i in range(len(v)):
                find=False
                if v[i] not in pos:
                    issub = False
                    break
                for p1 in pos[v[i]]:
                    if p1>p:
                        p=p1
                        find=True
                        break
                if not find:
                    issub=False
                    break
            if issub:
                res.append(v)
        return len(res)
