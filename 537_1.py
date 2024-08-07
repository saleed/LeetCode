#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 18:43
# @Author  : sunaolin
# @File    : 537_1.py
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        r1,v1=self.extractValue(num1)
        r2,v2=self.extractValue(num2)

        r=r1*r2-v1*v2
        v=r1*v2+r2*v1
        return str(r)+"+"+str(v)+"i"

    def extractValue(self,s):
        real=""
        virtual=""
        i=0
        while i<len(s) and s[i].isdigit():
            i+=1
        real=s[:i]
        j=i+1
        while j<len(s) and s[j]!="i":
            j+=1
        virtual=s[i+1:j]

        return int(real),int(virtual)