#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 15:32
# @Author  : sunaolin
# @File    : 769.py


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i=0
        res=0
        while i<len(arr):
            j=i
            end=i
            while True:
                end=max(end,arr[j],arr.index(arr[j]))
                if j==end:
                    break
                j+=1
            res+=1
            i=end+1
        return res
