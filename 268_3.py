#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 14:13
# @Author  : sunaolin
# @File    : 268_3.py


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        while p<len(nums):
            i=p
            pre=float("inf")
            while nums[i]<len(nums) and nums[i]!=i and nums[i]!=pre:
                nums[i],nums[nums[i]]=nums[nums[i]],nums[i]
                pre=nums[i]
        for i in range(len(nums)):
            if nums[i]!=i:
                return i

