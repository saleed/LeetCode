#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/19 13:43
# @Author  : sunaolin
# @File    : 34_7.py


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]

        p=0
        q=len(nums)-1
        while p<q:
            mid=(p+q)/2
            if nums[mid]>=target:
                q=mid
            else:
                p=mid+1
        left=-1
        if nums[p]==target:
            left=p
        p = 0
        q = len(nums) - 1
        while p<q:
            mid=(p+q+1)/2
            if nums[mid]<=target:
                p=mid
            else:
                q=mid-1
        right=-1
        if nums[p]==target:
            right=p
        return [left,right]