#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 14:23
# @Author  : sunaolin
# @File    : 213_3.py


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return max(nums)

        dp=[0]*len(nums)
        dp[0]=0
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        print("1",dp)
        max1=max(dp)
        dp[0]=nums[0]
        # dp[1] = 0  注意这里不是0
        dp[1]=nums[0] ##注意这里初始化
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print("2",dp)
        max2=max(dp[:-1])
        return max(max1,max2)