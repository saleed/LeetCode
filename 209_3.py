#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 11:16
# @Author  : sunaolin
# @File    : 209_3.py
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: xist[int]
        :rtype: int
        """
        p=0
        q=0
        maxl=float("inf")
        tmpsum=0
        while q<len(nums):
            while q<len(nums) and tmpsum<target:
                tmpsum+=nums[q]
                q+=1
            while tmpsum>=target:  ###在更新边界的时候，更新到每个可能的区间
                maxl = min(maxl, q-p)
                tmpsum-=nums[p]
                p+=1
        return maxl if maxl!=float("inf") else 0








