#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 11:35
# @Author  : sunaolin
# @File    : 22_6.py

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(res,"",0,0,n)



    def dfs(self,res,tmp,ln,rn,n):
        if ln==rn==n:
            res.append(tmp)
            return
        if ln==rn:
            tmp+="("
            ln+=1
            self.dfs(res,tmp,ln,rn,n)
        elif ln==n:
            tmp+=")"
            rn+=1
            self.dfs(res, tmp, ln, rn, n)
        else:
            newtmp =tmp+ ")"
            self.dfs(res,newtmp, ln, rn+1, n)
            newtmp=tmp+"("
            self.dfs(res,newtmp,ln+1,rn,n)

