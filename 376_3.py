#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 23:54
# @Author  : sunaolin
# @File    : 376_3.py


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high=[0]*len(nums)
        low=[0]*len(nums)
        high[0]=1
        low[0]=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                high[i]=max(high[i-1],low[i-1]+1)
                low[i]=low[i-1]
            elif nums[i]<nums[i-1]:
                high[i]=high[i-1]
                low[i]=max(low[i-1],high[i-1]+1)
            else:
                high[i]=high[i-1]
                low[i]=low[i-1]
        return max(low[-1],high[-1])