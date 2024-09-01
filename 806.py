#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 13:24
# @Author  : sunaolin
# @File    : 806.py


class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        row=1
        l=0
        for v in s:
            if l+widths[ord(v)-ord('a')]>100:
                row+=1
                l=v
            else:
                l+=widths[ord(v)-ord('a')]
        return [row,l]
