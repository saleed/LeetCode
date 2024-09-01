#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 16:20
# @Author  : sunaolin
# @File    : 836.py


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec1[3]<=rec2[1] or rec1[1]>=rec2[3] or rec1[0]>=rec2[2] or rec1[2]<=rec2[0]:
            return False
        return True
