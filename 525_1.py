#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 10:24
# @Author  : sunaolin
# @File    : 525_1.py

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff01=0
        vdict={0:-1}
        maxl=0
        for i in range(len(nums)):
            if nums[i]==1:
                diff01+=1
            else:
                diff01-=1

            if diff01 in vdict:
                maxl=max(maxl,i-vdict[diff01])
            else:
                vdict[diff01]=i
        return maxl


