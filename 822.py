#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 16:39
# @Author  : sunaolin
# @File    : 822.py


class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """

        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                return 0
            minv=min(fronts[i],backs[i],minv)
        return minv
