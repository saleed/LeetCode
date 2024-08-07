#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/31 18:57
# @Author  : sunaolin
# @File    : 553_1.py

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==0:
            return ""
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0])+"/"+str(nums[1])

        res=str(nums[0])+"/"+"("
        for v in nums[1:]:
            res+=str(v)+"/"
        res=res[:-1]
        res+=")"
        return res
