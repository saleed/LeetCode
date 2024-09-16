#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 16:15
# @Author  : sunaolin
# @File    : 852.py


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        p=0
        q=len(arr)-1
        while p<q:
            mid=(p+q)/2
            if p>0 and  arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            if arr[mid-1]<arr[mid]<arr[mid+1]:
                p=mid+1
            else:
                q=mid
        return p

