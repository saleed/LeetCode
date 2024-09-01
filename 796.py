#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 19:29
# @Author  : sunaolin
# @File    : 796.py


class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
        return False