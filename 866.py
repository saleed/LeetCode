#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 15:08
# @Author  : sunaolin
# @File    : 866.py


class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """

        nl=len(str(n))
        for i in range(pow(10,nl/2)+1,pow(10,nl/2+1)):
            if i<n:
                continue
            else:




    def isprime(self,n):

        sqt=math.sqrt(n)
        for i in range(2,sqt+1):
            if n%i==0:
                return False

        return True