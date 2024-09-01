#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/9 16:57
# @Author  : sunaolin
# @File    : 696.py


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count=[]

        pre=-1
        cnt=0
        for v in s:
            if v==pre:
                cnt+=1
            else:
                count.append(cnt)
                pre=v
                cnt=1
        count.append(cnt)
        res=0
        for i in range(len(count)-1):
            res+=min(count[i],count[i+1])
        return res
