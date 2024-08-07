#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 16:27
# @Author  : sunaolin
# @File    : 290_4.py


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        wdict={}
        pdict={}
        sp=s.split(" ")
        if len(pattern)!=len(sp):
            return True

        for i in range(len(pattern)):
            if (pattern[i] in pdict and pdict[pattern[i]]!=sp[i]) or(sp[i] in wdict and wdict[sp[i]]!=pattern[i]):
                return False
            if pattern[i] not in pdict and sp[i] not in wdict:
                pdict[pattern[i]]=sp[i]
                wdict[sp[i]]=pattern[i]
        return True
