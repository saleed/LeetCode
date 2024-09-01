#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 15:09
# @Author  : sunaolin
# @File    : 819.py


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words=self.extract(paragraph)
        freq={}
        maxf=0
        res=""
        for v in words:
            if v in banned:
                continue
            if v in freq:
                freq[v]+=1
            else:
                freq[v]=1
            if freq[v]>maxf:
                maxf=freq[v]
                res=v
        return res





    def extract(self,s):
        i=0
        res=[]
        while i<len(s):
            j=i
            while j<len(s) and s[j].isalpha():
                j+=1
            if i!=j:
                res.append(s[i:j].lower())
                i=j
            else:
                i+=1
        return res
