#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 13:25
# @Author  : sunaolin
# @File    : 325_1.py

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefixsum={}

        maxl=0
        presum=0
        for i in range(len(nums)):
            presum+=nums[i]
            if presum not in prefixsum:
                prefixsum[presum]=i
            if presum==k:
                maxl=max(maxl,i+1)
            if presum-k in prefixsum:
                maxl=max(maxl,i-prefixsum[presum-k])
        return maxl


