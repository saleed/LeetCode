#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 17:28
# @Author  : sunaolin
# @File    : 826.py


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        pft = 0

        for v in worker:
            maxprofit=0

            for i in range(len(difficulty)):
                if v<difficulty[i]:
                    break
                maxprofit=max(maxprofit,profit[i])
            pft+=maxprofit
        return pft




