#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 11:29
# @Author  : sunaolin
# @File    : 152_3.py


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        pos=[-float("inf")]*len(nums)
        neg=[float("inf")]*len(nums)


        if nums[0]==0:
            pos[0]=0
            neg[0]=0
        elif nums[0]>0:
            pos[0]=nums[0]
        else:
            neg[0]=nums[0]



        for i in range(1,len(nums)):
            if nums[i]>0:
                pos[i]=max(nums[i],nums[i]*pos[i-1])
                neg[i]=min(nums[i],nums[i]*neg[i-1])
            elif nums[i]<0:
                pos[i] = max(nums[i], nums[i] * neg[i - 1])
                neg[i] = min(nums[i], nums[i] * pos[i - 1])
            else:
                pos[i]=0
                neg[i]=0
        return max(max(pos),max(neg))


