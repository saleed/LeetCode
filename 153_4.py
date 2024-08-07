#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 13:58
# @Author  : sunaolin
# @File    : 153_4.py


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        q=len(nums)-1
        while p<q:
            mid=int((p+q)/2)
            if nums[mid]<nums[q]:  ###mid和q一定不同，所以判断区间的时候可以直接排除正序区间
                q=mid
            else:
                p=mid+1
        return nums[p]
