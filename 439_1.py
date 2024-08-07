#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 15:32
# @Author  : sunaolin
# @File    : 439_1.py

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        i=0
        while i<len(expression):
            if i+1<len(expression) and expression[i]=="T" and expression[i+1]=="?" :
                i+=2
            elif i+1<len(expression) and expression[i]=="F" and expression[i+1]=="?":
                i+=4
            else:
                return expression[i]


