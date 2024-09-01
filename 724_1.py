#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/14 17:19
# @Author  : sunaolin
# @File    : 724_1.py

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumv=sum(nums)
        tmpsum=0
        for i in range(len(nums)):
            if tmpsum==sumv-tmpsum-nums[i]:
                return i
            tmpsum+=nums[i]
        return -1
