#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 16:19
# @Author  : sunaolin
# @File    : 673_1.py


class Solution(object):
    def findNumberOfLIS(self, nums):
        """fdfdf
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        maxl=0
        maxcnt=0

        for i in range(len(nums)):
            if maxl == 1:
                maxcnt += 1
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    if dp[j]+1>maxl:
                        maxl=dp[j]+1
                        maxcnt=1
                    elif dp[j]+1==maxl:
                        maxcnt+=1

        print(dp)
        return maxcnt

