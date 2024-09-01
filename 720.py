#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 14:47
# @Author  : sunaolin
# @File    : 720.py


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        wdict={}

        for v in words:
            wdict[v]=1

        words.sort(key=lambda x:(-len(x),x))
        print(words)
        # words=words[::-1]
        for v in words:
            if self.check(v,wdict):
                return v




    def check(self,word,wdict):
        for i in range(1,len(word)+1):
            if word[:i] in wdict:
                continue
            else:
                return False
        return True





