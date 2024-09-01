#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 15:07
# @Author  : sunaolin
# @File    : 747.py

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        pdict={}
        res=""
        minl=float("inf")

        for l in licensePlate:
            if l.isalpha():
                if l.lower() in pdict:
                    pdict[l.lower()]+=1
                else:
                    pdict[l.lower()]=1

        for w in words:
            wdict=self.cNum(w)
            flag=1
            for k in pdict:
                if k in wdict and wdict[k]>=pdict[k]:
                    continue
                else:
                    flag=0
                    break
            if flag and minl>len(w):
                minl=len(w)
                res=w
        return res










    def cNum(self,word):
        cdict={}
        for v in word:
            if v in cdict:
                cdict[v]+=1
            else:
                cdict[v]=1
        return cdict

