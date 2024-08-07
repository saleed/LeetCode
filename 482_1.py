#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 11:05
# @Author  : sunaolin
# @File    : 482_1.py


class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        cnt=0
        res=""
        for i in range(len(s))[::-1]:
            if s[i]=="-":
                continue
            else:
                if s[i].isalpha():
                    res+=s[i].upper()
                else:
                    res+=s[i]
                cnt+=1
                if cnt==k:
                    res+="-"
                    cnt=0
        if len(res)>0 and res[-1]=="-":
            return res[:-1][::-1]

        return res[::-1]