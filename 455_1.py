#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 16:57
# @Author  : sunaolin
# @File    : 455_1.py

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        p=0
        cnt=0
        for i in range(len(g)):
            while p<len(s) and s[p]<g[i]:
                p+=1
            if p<len(s):
                cnt+=1
            p+=1
        return cnt




