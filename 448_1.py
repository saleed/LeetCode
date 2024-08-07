#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 22:34
# @Author  : sunaolin
# @File    : 448_1.py

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            pre=float("inf")
            while nums[nums[i]-1]!=nums[i] and nums[i]!=pre:
                pre = nums[i]
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        res=[]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
