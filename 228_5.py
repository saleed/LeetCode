#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 17:28
# @Author  : sunaolin
# @File    : 228_5.py


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(float("inf"))
        start=0
        res=[]
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                continue
            else:
                if start==nums[i]:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(nums[i]))
                    start=nums[i+1]
        return res


