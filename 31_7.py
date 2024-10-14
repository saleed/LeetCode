#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 19:59
# @Author  : sunaolin
# @File    : 31_7.py



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        id=-1
        for i in range(1,len(nums))[::-1]:
            if nums[i-1]>nums[i]:
                continue
            else:
                id=i-1
        if id==-1:
            return nums[::-1]

        for j in range(len(nums)):
            if nums[j]>nums[id]:
                nums[i],nums[j]=nums[j],nums[i]
                break
        p=id+1
        q=len(nums)
        while p<q:
            nums[p],nums[q]=nums[q],nums[p]
            p+=1
            q-=1
        return nums

