#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/22 19:36
# @Author  : sunaolin
# @File    : 81_2.py


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        p=0
        q=len(nums)-1
        while p<q:
            mid=(p+q)/2
            if nums[mid]==target:
                return True

            if nums[mid]==nums[p]:
                p+=1
            if nums[p]<nums[mid]:
                if nums[p]<=target<nums[mid]:
                    q=mid
                else:
                    p=mid+1
            else:
                if nums[mid]<target<=nums[q]:
                    p=mid+1
                else:
                    q=mid
        return nums[p]==target
