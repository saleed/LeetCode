#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 23:36
# @Author  : sunaolin
# @File    : 300——1.py

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

