#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 16:54
# @Author  : sunaolin
# @File    : 453.py

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            res += nums[i] - min(nums)
        return res
