#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 16:34
# @Author  : sunaolin
# @File    : 791.py


class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        freq={}
        for v in s:
            if v in freq:
                freq[v]+=1
            else:
                freq[v]=1

        res=""
        for v in order:
            if v in freq:
                res+="v"*freq[v]
                del freq[v]
        for k in freq:
            res+=freq[k]*k
        return res