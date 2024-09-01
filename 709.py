#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/12 18:04
# @Author  : sunaolin
# @File    : 709.py

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for v in s:
            if v.isupper():
                res+=v.lower()
            else:
                res+=v
        return res