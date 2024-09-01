#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 10:29
# @Author  : sunaolin
# @File    : 830.py


class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        pre=0
        res=[]
        for i in range(len(s)):
            if s[i]!=s[pre]:
                if i-pre>=3:
                    res.append([pre,i-1])
                pre=i
        if len(s)-pre>=3:
            res.append([pre,len(s)-1])
        return res


