#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 15:03
# @Author  : sunaolin
# @File    : 781.py

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        vdict={}
        for i in range(len(answers)):
            if answers[i] in vdict:
                vdict[answers[i]]+=1
            else:
                vdict[answers[i]]=1

        res=0
        while True:
            sel=-1
            for k in vdict:
                if vdict[k]<=0:
                    continue
                if vdict[k]<k+1:
                    res+=k+1
                    sel=k
                    break
            if sel==-1:
                return res
            vdict[sel]-=(sel+1)
            res+=(sel+1)




