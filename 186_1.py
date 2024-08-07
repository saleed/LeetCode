#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 19:42
# @Author  : sunaolin
# @File    : 186_1.py




class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        p=0
        q=len(s)-1
        self.swap(s,p,q)
        # s.append(" ")
        p=0
        q=0
        while True:
            while q<len(s) and s[q]!=" ":
                q+=1
            self.swap(s,p,q-1)
            if q==len(s):
                return
            p=q+1
            q=p





    def swap(self,s,p,q):
        while p < q:
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1

