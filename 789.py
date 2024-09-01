#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 15:43
# @Author  : sunaolin
# @File    : 789.py


class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        minghost=float("inf")

        for v in ghosts:
            if abs(v[0]-target[0])+abs(v[1]-target[1])<minghost:
                minghost=abs(v[0]-target[0])+abs(v[1]-target[1])

        return abs(target[0])+abs(target[1])<minghost