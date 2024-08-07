#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/21 16:31
# @Author  : sunaolin
# @File    : 53_6.py


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
        return max(dp)