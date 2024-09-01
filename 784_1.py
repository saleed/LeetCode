#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 17:08
# @Author  : sunaolin
# @File    : 784_1.py


class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        self.dfs(s,0,"",res)
        return res

    def dfs(self,s,i,tmp,res):
        if i==len(s):
            res.append(tmp[:])
            return
        if s[i].isdigit():
            tmp+=s[i]
            self.dfs(s,i+1,tmp,res)
        else:
            tmp+=s[i]
            self.dfs(s,i+1,tmp,res)
            tmp=tmp[:-1]
            if s[i].upper()==s[i]:
                tmp+=s[i].lower()
            else:
                tmp+=s[i].upper()
            self.dfs(s,i+1,tmp,res)