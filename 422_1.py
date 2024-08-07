#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 14:58
# @Author  : sunaolin
# @File    : 422-1.py

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            if len(words[i])>len(words):
                return False
        # 完全不行
        for i in range(len(words)):
            for j in range(len(words[i])):
                c1=words[i][j]
                c2=words[j][i] if j<len(words) and i<words[j] else ""
                if c1==c2:
                    continue
                return False
        return True

