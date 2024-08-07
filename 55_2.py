#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 12:47
# @Author  : sunaolin
# @File    : 55——2.py


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """



        ##超时
        # dp=[False]*len(nums)
        # dp[0]=True
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if dp[j] and j+nums[j]>=i:
        #             dp[i]=True
        #             break
        # return dp[-1]


        maxreach=nums[0]
        for i in range(len(nums)):
            if maxreach<i:
                return False
            maxreach=max(maxreach,i+nums[i])
        return True





