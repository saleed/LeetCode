#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 19:40
# @Author  : sunaolin
# @File    : 523_1.py

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        leftdict={}
        presum=0

        for i in range(len(nums)):
            presum+=nums[i]
            left=presum%k
            if left in leftdict and i-leftdict[left]>2:
                return True
            leftdict[left]=i
        return False