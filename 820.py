#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 15:15
# @Author  : sunaolin
# @File    : 820.py


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s=""
        sdict={}
        words.sort(key=lambda x:len(x))

        for v in words[::-1]:
            if v in sdict:
                continue
            else:
                s+=v+"#"
                for j in range(len(v)-1):
                    sdict[v[j:]]=1
        return len(s)








