#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 10:44
# @Author  : sunaolin
# @File    : 80——3.py

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pre=float("inf")
        prenum=0
        p=0
        for i in range(len(nums)):
            if nums[i]==pre:
                if prenum==2:
                    continue
                else:
                    nums[p]=nums[i]
                    prenum+=1
                    p += 1
            else:
                prenum=1
                pre=nums[i]
                nums[p]=nums[i]
                p+=1
        return p


