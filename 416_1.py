#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/19 15:58
# @Author  : sunaolin
# @File    : 416_1.py


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # sumN=sum(nums)
        # if sumN%2==1:
        #     return False
        # return self.dfs(nums,0,0,sumN/2)
        return self.dp(nums)


    def dfs(self,nums,i,tmp,target):
        if tmp==target:
            return True
        if tmp<target and i<len(nums):
            return self.dfs(nums,i+1,tmp+nums[i],target) or self.dfs(nums,i+1,tmp,target)

    def dp(self,nums):
        dp=[[False for _ in range(sum(nums)/2+1)] for _ in range(len(nums))]
        dp[0][nums[0]] = True

        for i in range(1,len(nums)):
            for j in range(sum(nums)/2+1):
                dp[i][j]=(dp[i-1][j] or (dp[i-1][j-nums[i]] if j-nums[i]>=0 else False))
            print(dp[i])
        return dp[-1][-1]