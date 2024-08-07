#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 15:39
# @Author  : sunaolin
# @File    : 494_1.py


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.dp(nums,target)


    def dp(self,nums,target):
        if len(nums)==0:
            return 0
        maxv=0
        for v in nums:
            if v>0:
                maxv+=v
            else:
                maxv+=-v
        dp=[[0 for _ in range(2*maxv+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                # dp[i][maxv+nums[0]]=1
                # dp[i][maxv-nums[0]]=1
                # #这里不能直接写=1
                dp[i][maxv + nums[0]] += 1
                dp[i][maxv - nums[0]] += 1
                continue  ###一定要continue
            for j in range(2*maxv+1):
                # dp[i][j]=dp[i-1][j]
                if 2*maxv+1>=j-nums[i]>=0:
                    dp[i][j]+=dp[i-1][j-nums[i]]
                if 0<=j+nums[i]<2*maxv+1:
                    dp[i][j] += dp[i-1][j+nums[i]]
        if target>maxv:
            return 0
        return dp[-1][target+maxv]





