#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 18:22
# @Author  : sunaolin
# @File    : 795.py


class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """

        ##怎么找比当前值小的最左边界
        last1=last2=-1
        res=0
        for i in range(len(nums)):
            if left<=nums[i]<=right:
                last1=i
            if nums[i]>right:
                last2=i
                last1=-1
            if last1!=-1:
                res+=last2-last1
        return res