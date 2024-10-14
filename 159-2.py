#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 13:18
# @Author  : sunaolin
# @File    : 159-2.py

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        pos = {}
        start = -1
        res = 0
        for i in range(len(s)):
            if len(pos) == 2 and s[i] not in pos:
                # print(i,s[i],pos)
                k = pos.keys()
                if pos[k[0]] < pos[k[1]]:
                    start = pos[k[0]]
                    del pos[k[0]]
                else:

                    start = pos[k[1]]
                    del pos[k[1]]
            res = max(res, i - start)
            pos[s[i]] = i
        return res




