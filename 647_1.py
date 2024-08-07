#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 14:35
# @Author  : sunaolin
# @File    : 647_1.py

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        cnt=0

        for i in range(len(s)):
            p=i
            q=i
            while p>=0 and q<len(s) and s[p]==s[q]:
                cnt+=1
                p-=1
                q+=1
            p=i
            q=i+1
            while p >= 0 and q < len(s) and s[p] == s[q]:
                cnt += 1
                p -= 1
                q += 1
        return cnt







