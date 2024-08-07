#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 14:31
# @Author  : sunaolin
# @File    : 491_1.py


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,0,[],res)

        return res

    def dfs(self,nums,i,tmp,res):
        if i==len(nums) and len(tmp)>1:
            if tmp not in res: ####list也支持hash操作
                res.append(tmp[:])
            return
        if i<len(nums):
            self.dfs(nums,i+1,tmp,res)
            if len(tmp)==0 or (len(tmp)>0 and nums[i]>=tmp[-1]):
                tmp.append(nums[i])
                self.dfs(nums,i+1,tmp,res)
                tmp.pop()
