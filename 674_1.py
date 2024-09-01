#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 17:14
# @Author  : sunaolin
# @File    : 674——1.py


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxl=1
        prel=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                prel+=1
            else:
                prel=1
            maxl=max(maxl,prel)
        return maxl
