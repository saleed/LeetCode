#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/12 17:54
# @Author  : sunaolin
# @File    : 186_2.py


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
        self.swap(s,0,len(s)-1)
        i=0
        start=0
        while i<len(s):
            if s[i]!=" ":
                self.swap(s,start,i-1)
                i=i+1
                start=i+1
            else:
                i+=1
        self.swap(s,start,i)
        return s





    def swap(self,s,p,q):
        p=0
        q=len(s)-1
        while p<q:
            s[q],s[p]=s[p],s[q]
            p+=1
            q-=1
