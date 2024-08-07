#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 16:05
# @Author  : sunaolin
# @File    : 442_1.py

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            while nums[i]!=nums[nums[i]-1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] ##这样写就不行？？？？
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        return [num for i, num in enumerate(nums) if num - 1 != i]