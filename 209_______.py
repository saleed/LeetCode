#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 15:54
# @Author  : sunaolin
# @File    : 209_3.py

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: xist[int]
        :rtype: int
        """
        p=-1
        q=0
        sumN=0
        res=float("inf")
        while q<len(nums):
            while q<len(nums) and sumN<=target:
                sumN += nums[q]
                q+=1
            while p<q and sumN>target:
                sumN-=nums[p+1]
                p+=1
            res = min(res, q-1-p)
        return res

