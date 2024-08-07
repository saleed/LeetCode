#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 14:09
# @Author  : sunaolin
# @File    : 202_3.py

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True

        vis=set()
        vis.add(n)
        while True:
            tmp=n
            pow=0
            while tmp:
                pow+=(tmp%10)**2
                tmp/=10
            if pow in vis:
                return False
            if pow==1:
                return True
            vis.add(pow)
            n=pow



