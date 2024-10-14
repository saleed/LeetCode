#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 17:14
# @Author  : sunaolin
# @File    : 869.py


class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p=0
        while len(str(pow(2,p)))!=len(str(n)):
            p+=1
        while len(str(pow(2,p)))==len(str(n)):
            if "".join(sorted(pow(2,p)))=="".join(sorted(n)):
                return True
            p+=1
        return False
