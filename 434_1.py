#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 13:49
# @Author  : sunaolin
# @File    : 434_1.py

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        cnt=0
        while i<len(s):
            if s[i]!=" ":
                while i<len(s) and s[i]!=" ":
                    i+=1
                cnt+=1
            else:
                i+=1
        return cnt