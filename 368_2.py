#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 17:06
# @Author  : sunaolin
# @File    : 368_2.py


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp=[0]*len(nums)
        bt=[-1]*len(nums)
        dp[0]=1
        maxid=-1
        maxl=-float("inf")
        for i in range(len(nums)):
            for j in range(i)[::-1]:
                if nums[i]%nums[j]==0:
                    dp[i]=dp[j]+1
                    bt[i]=j
                    break  ##这里是否可以直接break 默认取到了如果nums[j]是nums[i]的约数，则不需要考虑小于是nums[j]之前的数
            if dp[i]>maxl:
                maxl=dp[i]
                maxid=i
        # print(dp)
        res=[]
        res.append(nums[maxid])
        tmp=bt[maxid]
        while tmp!=-1:
            res.append(nums[tmp])
            tmp=bt[tmp]
        return res[::-1]






