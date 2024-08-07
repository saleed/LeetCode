#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 13:44
# @Author  : sunaolin
# @File    : 621_1.py

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tdict={}
        for v in tasks:
            if v in tdict:
                tdict[v]+=1
            else:
                tdict[v]=1
        flag=1
        while flag:
            flag=0
            for k in
