#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 11:17
# @Author  : sunaolin
# @File    : 567_1.py


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        i=0
        while i<len(s2):
            s=list(s1)
            while i<len(s2) and s2[i] in s and len(s)>0:
                s.remove(s2[i])
                i+=1
            if len(s)==0:
                return True
            i+=1
        return False

print(list("ab"))
