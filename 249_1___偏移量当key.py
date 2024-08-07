#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/8 10:47
# @Author  : sunaolin
# @File    : 249_1.py

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        gdict={}
        for v in strings:
            key=self.gethashkey(v)
            if key in gdict:
                gdict[key].append(v)
            else:
                gdict[key]=[v]
        return gdict.values()

    def gethashkey(self,v):
        key=""
        minch="z"
        for i in range(len(v)):
            minch=min(minch,v[i])
        for i in range(len(v)):
            diff=ord(v[i])-ord(minch)
            key+=chr(ord(v[i])-diff)
        return key




