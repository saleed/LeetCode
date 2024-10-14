#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 19:55
# @Author  : sunaolin
# @File    : 168_4.py


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res=""
        columnNumber-=1
        while columnNumber:
            c=columnNumber%26
            res=chr(ord('A')+c)+res
            columnNumber=columnNumber/26
