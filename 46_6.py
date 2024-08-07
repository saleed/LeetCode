#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 19:24
# @Author  : sunaolin
# @File    : 46_6.py

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,0,res)
        return res

    ##不含重复数字的数组

    def dfs(self,nums,i,res):
        if i==len(nums):
            res.append(nums[:])
            return
        self.dfs(nums, i + 1, res)
        for j in range(i+1,len(nums)):
            if nums[j]==nums[i]:
                continue
            nums[i],nums[j]=nums[j],nums[i]
            self.dfs(nums,i+1,res)
            nums[i], nums[j] = nums[j], nums[i]

