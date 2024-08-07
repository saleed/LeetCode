#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 15:05
# @Author  : sunaolin
# @File    : 159.py


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxl=-float("inf")
        chd=dict()
        for i in range(len(s)):
            if s[i] in chd:
                chd[s[i]][1]=i
            else:
                if len(chd)<2:
                    chd[s[i]]=[i,i]
                else:
                    k=chd.keys()
                    if chd[k[0]][1]<chd[k[1]][1]:
                        chd[k[1]][0]=max(chd[k[1]][0],chd[k[0]][1])
                        del chd[k[0]]
                    else:
                        chd[k[0]][0] = max(chd[k[0]][0], chd[k[1]][1])
                        del chd[k[1]]
                    chd[s[i]]=[i,i]
            leftbound=chd.values()
            maxl=i-min(leftbound[0][0],leftbound[0][1])
        return maxl



s =
"abaccc"
a


