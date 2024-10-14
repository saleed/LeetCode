#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/2 15:48
# @Author  : sunaolin
# @File    : 75_6.py

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p=0
        q=0
        r=len(nums)-1
        while p<=r:
            if nums[p]==0:
                nums[p],nums[q]=nums[q],nums[p]
                p+=1
                q+=1
            elif nums[p]==2:
                nums[p],nums[r]=nums[r],nums[p]
                r-=1
            else:
                p+=1
            print(p,q,r,nums)


