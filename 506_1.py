#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 14:04
# @Author  : sunaolin
# @File    : 506_1.py


class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorts=score[:]
        sorts.sort()
        res=[]
        for v in score:
            if sorts.index(v)==len(score)-1:
                res.append("Gold Medal")
            elif sorts.index(v)==len(score)-2:
                res.append("Silver Medal",)
            elif sorts.index(v)==len(score)-3:
                res.append("Bronze Medal")
            else:
                res.append(str(len(score)-sorts.index(v)))
        return res

