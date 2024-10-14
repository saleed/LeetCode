#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 16:21
# @Author  : sunaolin
# @File    : 14_7.py

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res=""
        i=0
        while True:
            if i>=len(strs[0]):
                return res
            tmp=strs[0][i]
            for v in strs:
                if i>=len(v) or v[i]!=tmp:
                    return res

            res+=tmp
            i+=1
        return res