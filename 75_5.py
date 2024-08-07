#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 18:17
# @Author  : sunaolin
# @File    : 74_5.py


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i=0
        p=0
        q=len(nums)-1
        while i<=q:####这里很重要 不能是i<len(nums)
            if nums[i]==0:
                nums[i],nums[p]=nums[p],nums[i]
                p+=1
                if i+1==p:
                    i+=1
            elif nums[i]==2:
                nums[i],nums[q]=nums[q],nums[i]
                q-=1
            else:
                i+=1

