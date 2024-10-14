#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 18:43
# @Author  : sunaolin
# @File    : 33_3.py


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """



        p=0
        q=len(nums)-1
        while p<q: ##p=
            mid=(p+q)/2
            if nums[p]<=nums[mid]:
                if nums[p]<=target<=nums[mid]:
                    q=mid
                else:
                    p=mid+1
            else:
                if nums[mid+1]<=target<=nums[q]:
                    p=mid+1
                else:
                    q=mid

        if nums[p]==target:
            return p
        return -1



