#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 15:01
# @Author  : sunaolin
# @File    : 581——1.py

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minv=[float("inf")]*len(nums) ##右到左最小的数
        maxv=[-float("inf")]*len(nums) ##左到右最大的数

        minvv=float("inf")
        maxvv=-float("inf")



        for i in range(len(nums)):
            if nums[len(nums)-1-i]<minvv:
                minv[len(nums)-1-i]=nums[len(nums)-1-i]
                minvv=nums[len(nums)-1-i]
            else:
                minv[len(nums) - 1 - i]=minvv

            if nums[i]>maxvv:
                maxv[i]=nums[i]
                maxvv=nums[i]
            else:
                maxv[i]=maxvv

        print(maxv)
        print(minv)

        left=len(nums)
        right=0
        for i in range(len(nums)):
            if minv[i]>=maxv[i]:
                left=min(left,i)
                right=max(right,i)
        return right-left+1

