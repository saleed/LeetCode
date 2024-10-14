#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/13 21:52
# @Author  : sunaolin
# @File    : 198_3.py


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##考虑第i个房间是否偷窃
        ##偷窃的话，则dp[i]=dp[i-2]+nums[i]
        ##不偷，dp[i]=dp[i-1]


        ##如果考虑更细一点，dp[i]保存两个状态偷或者不偷的最大收益

        dp=[0]*len(nums)
        if len(nums)>0:
            dp[0]=nums[0]
        if len(nums)>1:
            dp[1]=max(nums[:2])

        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return max(dp)

