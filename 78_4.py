#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/24 19:38
# @Author  : sunaolin
# @File    : 78_4.py

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """



    def dfs(self,nums,i,tmp,res):
        if i>=len(nums):
            res.append(tmp[:])
            return
        self.dfs(nums,i+1,tmp,res)
        tmp.append(nums[i])
        self.dfs(nums,i+1,tmp,res)
        tmp.pop()  ###为什么这里要pop掉？？？ 树状遍历画一下树状图

