#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 09:53
# @Author  : sunaolin
# @File    : 325_1.py

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        presum=[0]*len(nums)
        maxl=1
        presum[0]=nums[0]
        for i in range(1,len(nums)):
            presum[i]=presum[i-1]+nums[i]
            if presum[i]==k:
                maxl=max(maxl,i+1)
            else:
                for j in range(i+1):
                    if presum[i]-presum[j]==k:
                        maxl=max(maxl,i-j)
        return maxl

