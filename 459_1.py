#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 20:58
# @Author  : sunaolin
# @File    : 459_1.py

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(1,int(len(s)/2)+1)[::-1]:
            if len(s)%i==0:
                T=len(s)/i
                cmp=s[:T]
                j=0
                while j+T<=len(s) and s[j:j+T]==cmp:
                    j+=T
                if j!=T:
                    continue
                else:
                    return True
        return False
