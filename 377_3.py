#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 00:15
# @Author  : sunaolin
# @File    : 377_3.py

###这道题目是默认nums>0的

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res={}
        return self.dfs(nums,target,res)


    def dp(self,nums,target):
        if len(nums) == 0:
            return
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]
        return dp[-1]

    ##dfs记忆化搜索
    def dfs(self,nums,target,res):
        if target==0:
            return 1
        if target in res:
            return res[target]
        if target>0:
            res[target]=0
            for i in range(len(nums)):
                ret=self.dfs(nums,target-nums[i],res)
                res[target]=max(res[target],ret)
            return res[target]
        return 0

