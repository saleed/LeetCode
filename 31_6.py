#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 15:59
# @Author  : sunaolin
# @File    : 31_6.py

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        id=-1
        for i in range(1,len(nums))[::-1]:
            if nums[i-1]>=nums[i]:
                continue
            else:
                id=i-1
                break
        if id!=-1:
            swap=-1
            for i in range(id+1,len(nums))[::-1]:
                if nums[i]>nums[id]:
                    swap=i
                    break  ###注意break
            nums[id],nums[swap]=nums[swap],nums[id]
            print(id,swap)
        p=id+1
        q=len(nums)-1
        while p<q:
            nums[p],nums[q]=nums[q],nums[p]
            p+=1
            q-=1
