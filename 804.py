#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 11:10
# @Author  : sunaolin
# @File    : 804.py
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        res=[]
        for v in words:
            ms=self.getMoss(v)
            if ms not in res:
                res.append(ms)
        return len(res)




    def getMoss(self,word):
        moss = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        res=""
        for v in word:
            res+=moss[ord(v)-ord('a')]
        return res
