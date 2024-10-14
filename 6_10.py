#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 13:54
# @Author  : sunaolin
# @File    : 6_10.py

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        T=2*numRows-2
        res=""
        for i in range(numRows):
            if i==0 or i==numRows-1:
                j=0
                while i+j*T<len(s):
                    res+=s[i+j*T]
                    j+=1
            else:
                j=0
                while i+j*T<len(s):
                    if i+j*T<len(s):
                        res+=s[i+j*T]
                    if T-i+j*T<len(s):
                        res+=s[T-i+j*T]
                    j+=1

        return res

