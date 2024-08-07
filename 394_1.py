#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 19:04
# @Author  : sunaolin
# @File    : 394_1.py


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.dfs(s)


    def dfs(self,s):
        if len(s)==0:
            return ""
        res=""
        i=0
        while i<len(s):
            if s[i].isdigit():
                d=""
                while i<len(s) and s[i]!="[":
                    d+=s[i]
                    i+=1
                n=int(d)
                i+=1
                st=1
                tmp="["
                while i<len(s) and st>0:
                    if s[i]=="]":
                        st-=1
                    elif s[i]=="[":
                        st+=1
                    tmp+=s[i]
                    i+=1
                res+=n*self.dfs(tmp[1:-1])##去除外层括号
            else:
                res+=s[i]
                i+=1
        return res