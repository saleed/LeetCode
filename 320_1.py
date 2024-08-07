#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 16:01
# @Author  : sunaolin
# @File    : 320_1.py

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res=[]
        self.dfs(word,"",res,0)
        self.dfs(word,"",res,1)
        return res



    def dfs(self,word,tmp,res,stat):
        if len(word)==0:
            res.append(tmp)
            return

        if stat==0:
            for i in range(len(word)):
                newtmp=tmp+str(i+1)
                self.dfs(word[i+1:],newtmp,res,1)
        else:
            for i in range(len(word)):
                newtmp=tmp+word[:i+1]
                self.dfs(word[i+1:],newtmp,res,0)
