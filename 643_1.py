#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 13:26
# @Author  : sunaolin
# @File    : 643_1.py


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        presum=0
        maxsum=0

        for i in range(len(nums)):
            presum+=nums[i]
            if i<k-1:
                continue
            else:
                maxsum=max(maxsum,presum)
                presum-=nums[i-(k-1)]
            print(maxsum,presum)
        return maxsum/k
