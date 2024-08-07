#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 13:47
# @Author  : sunaolin
# @File    : 485_1.py


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        cnt=0
        maxl=0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt=0
            else:
                cnt+=1
            maxl=max(maxl,cnt)
        return maxl