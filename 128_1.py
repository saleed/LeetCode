#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 15:53
# @Author  : sunaolin
# @File    : 128_1.py



class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=1
        for v in nums:
            if v-1 not in nums:
                y=v
                while y in nums:
                    y+=1
                res=max(res,y-v)
        return res




