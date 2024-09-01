#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 13:52
# @Author  : sunaolin
# @File    : 744.py


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        mindif=100
        minc=""
        for v in letters:
            if v>target and ord(v)-ord(target)<mindif:
                mindiff=ord(v)-ord(target)
                minc=v
        return minc