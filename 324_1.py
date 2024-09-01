#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 18:09
# @Author  : sunaolin
# @File    : 324_1.py


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag=True

        for i in range(len(nums)-1):
            if (flag and nums[i]>nums[i+1]) or (not flag and nums[i]<nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]