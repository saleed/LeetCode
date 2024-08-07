#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 21:50
# @Author  : sunaolin
# @File    : 41_5.py

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            tmpi=i
            pre=float("inf")
            while nums[tmpi]>0 and nums[tmpi]<=len(nums) and nums[tmpi]!=tmpi+1:
                tmp=nums[nums[tmpi]-1]
                nums[nums[tmpi]-1]=nums[tmpi]
                nums[tmpi]=tmp
                if nums[tmpi]==pre:
                    break
                pre=nums[tmpi]


        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1