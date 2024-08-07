#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 11:01
# @Author  : sunaolin
# @File    : 565_1.py

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vis=set()
        vis.add(0)
        lmax=0
        for i in range(len(nums)):
            if nums[i] in vis:
                continue
            else:
                j=0
                l=1
                while nums[j] not in vis:
                    l+=1
                    vis.add(nums[j])
                    j=nums[j]
                lmax=max(lmax,l)
        return lmax