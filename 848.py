#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/31 16:05
# @Author  : sunaolin
# @File    : 848.py


class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """

        shift=[0]*len(shifts)
        sumv=0
        for i in range(len(shifts)):
            shift[i]=sum(shifts)-sumv
            sumv += shifts[i]
        res=""
        for i in range(len(s)):
            suffix=ord(s[i])+shift[i]
            if suffix>ord('z'):
                suffix-=26
            res+=chr(suffix)
            print(res)
        return res


