#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/30 17:02
# @Author  : sunaolin
# @File    : 844.py

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        st1=[]
        st2=[]
        for v in s:
            if v=="#":
                if len(st1)>0:
                    st1.pop()
            else:
                st1.append(v)
        for v in t:
            if v == "#":
                if len(st2) > 0:
                    st2.pop()
            else:
                st2.append(v)
        return "".join(st1)=="".join(st2)
