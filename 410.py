#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 17:25
# @Author  : sunaolin
# @File    : 410.py


class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp=[[float("inf") for _ in range(k+1)] for _ in range(len(nums))]

        for j in range(k + 1): ###一定要注意先后
            for i in range(len(nums)):
                if j==0:
                    dp[i][j]=sum(nums[:i+1])
                else:
                    for s in range(i):
                        if s<j-1:
                            continue
                        dp[i][j]=min(dp[i][j],max(dp[s][j-1],sum(nums[s:i+1])))

        for v in dp:
            print(v)
        return dp[-1][-1]


nums =[1,4,4]
k =3
a=Solution()
print(a.splitArray(nums,k))