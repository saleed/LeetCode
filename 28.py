#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 19:46
# @Author  : sunaolin
# @File    : 28.py


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1