#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/3 11:54
# @Author  : sunaolin
# @File    : 78_5.py

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,0,[],res)
        return res

    def dfs(self,nums,i,tmp,res):
        if i==len(nums):
            res.append(tmp[:])
            return
        self.dfs(nums,i+1,tmp,res)
        tmp.append(nums[i])
        self.dfs(nums,i+1,tmp,res)
        tmp.pop()