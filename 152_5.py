#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/12 17:36
# @Author  : sunaolin
# @File    : 152_5.py



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 and nums[0]<0:
            return nums[0]
        pos=[0]*len(nums)
        neg=[0]*len(nums)
        if nums[0]==0:
            pos[0]=0
            neg[0]=0
        elif nums[0]>0:
            pos[0]=nums[0]
        else:
            neg[0]=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==0:
                pos[i]=0
                neg[i]=0
            elif nums[i]>0:
                pos[i]=max(nums[i],nums[i]*pos[i-1])
                neg[i]=nums[i]*neg[i-1]
            else:
                pos[i]=nums[i]*neg[i-1]
                neg[i]=min(nums[i],nums[i]*pos[i-1])

        return max(pos)