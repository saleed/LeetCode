#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 10:12
# @Author  : sunaolin
# @File    : 816.py
class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s=s[1:-1]
        res=[]
        for i in range(len(s)-1):
            left=s[:i+1]
            right=s[i+1:]
            print(left,right)
            l=self.addDot(left)
            r=self.addDot(right)
            if len(l)>0 and len(r)>0:
                for p in l:
                    for q in r:
                        res.append("("+p+", "+q+")")
        return res

    def addDot(self,s):
        if s=="":
            return []
        res=[]
        if s[0]!='0' or (len(s)==1 and s=='0'):
            res.append(s)
        for i in range(len(s)-1):
            if self.checkBeforeDot(s[:i+1]) and self.checkAfterDot(s[i+1:]):
                res.append(s[:i+1]+"."+s[i+1:])
        return res

    def checkBeforeDot(self,s):
        if len(s)==0:
            return False
        if s[0]!='0' or (s=='0' and len(s)==1):
            return True
        return False

    def checkAfterDot(self,s):
        if len(s)==0:
            return False
        if s[-1]!="0":
            return True
        return False




