#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 16:41
# @Author  : sunaolin
# @File    : 243_2.py

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = float("inf")
        pos2 = -float("inf")
        mind = float("inf")

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
            if wordsDict[i] == word2:
                pos2 = i

            mind = min(mind, abs(pos1 - pos2))
        return mind
