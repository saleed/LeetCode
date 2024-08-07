#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 16:56
# @Author  : sunaolin
# @File    : 171_1.py


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res=0
        for i in range(len(columnTitle)):
            res*=26
            res+=((ord(columnTitle[i])-ord('A'))+1)
        return res
