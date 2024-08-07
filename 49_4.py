#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 19:41
# @Author  : sunaolin
# @File    : 49_4.py

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = {}
        for v in strs:
            k = self.getHashKey(v)
            if k in res:
                res[k].append(v)
            else:
                res[k] = [v]
        return res.values()

    def getHashKey(self, s):
        k = [0] * 26
        for i in range(len(s)):
            k[ord(s[i]) - ord('a')] += 1

        return tuple(k)

