#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 15:31
# @Author  : sunaolin
# @File    : 683.py


class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type k: int
        :rtype: int
        """

        bubopen={}

        for i in range(len(bulbs)):
            if bulbs[i] in bubopen:
                del bubopen[bulbs[i]]
            else:
                bubopen[bulbs[i]]=i
            for k in bubopen:
                if abs(k-bulbs[i])==k+1:
                    return i+1

        return -1