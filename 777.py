#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 14:06
# @Author  : sunaolin
# @File    : 777.py


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i=0
        j=0

        while True:
            while i<len(start) and start[i]=='X':
                i+=1
            while j<len(end) and end[j]=='X':
                j+=1
            if i<len(start) and j<len(end):
                if start[i]!=end[j] or (end[j]=="L" and j>i) or (end[j]=="R" and j<i):
                    return False
                else:
                    i+=1
                    j+=1
            else:
                break
        return i==len(start) and j==len(end)




