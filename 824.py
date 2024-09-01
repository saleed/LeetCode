#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 16:56
# @Author  : sunaolin
# @File    : 824.py

class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        res=""
        spt=sentence.split(" ")
        for i in range(len(spt)):
            if spt[i][0].lower() in ('a', 'e', 'i', 'o', 'u'):
                res+=spt[i]+"ma"+(i+1)*'a'+" "
            else:
                res+=spt[i][1:]+spt[i][0]+"ma"+(i+1)*'a'+" "
        return res[:-1]





