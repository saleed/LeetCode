#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 11:05
# @Author  : sunaolin
# @File    : 162_3.py


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 11:05
# @Author  : sunaolin
# @File    : 162_3.py



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[-float("inf")]+nums+[-float("inf")]
        p=1
        q=len(nums)-1  ####注意这里的p从1开始，q需要从加了nums的尾部开始，
        while p<q:
            mid=int((p+q)/2)
            print(mid)
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid-1
            elif nums[mid-1]<nums[mid]:
                p=mid+1
            else:
                q=mid
        return p-1 #####头部append了一个数，需要结果减一