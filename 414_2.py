#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/19 15:40
# @Author  : sunaolin
# @File    : 414_2.py

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=-float("inf")
        max2=-float("inf")
        max3=-float("inf")

        for i in range(len(nums)):
            if nums[i]>max1:
                max3=max2
                max2=max1
                max1=nums[i]
            elif nums[i]>max2:
                max3=max2
                max2=nums[i]
            elif nums[i]>max3:
                max3=nums[i]
        return max3 if max3!=-float("inf") else max2 if max2!=-float("inf") else max1 if max1!=-float("inf") else max1

