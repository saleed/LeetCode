#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/22 17:53
# @Author  : sunaolin
# @File    : 66_2.py


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        c=1
        for i in range(len(digits))[::-1]:
            tmp=(digits[i]+c)
            digits[i]=tmp%10
            c=tmp/10
        if c:
            digits=[1]+digits
        return digits
