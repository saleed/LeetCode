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
            k[ord(s[i]) - ord('a')] += 1  ####注意这里不能使用移位的方式使用 移位的k无法统计个数

        return tuple(k)  ##只有tuple才能当做haskkey

