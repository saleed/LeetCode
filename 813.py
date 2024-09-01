#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 18:49
# @Author  : sunaolin
# @File    : 813.py


class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        dp=[[0 for _ in range(k+1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(1,k+1):
                # print(i, j)
                if j==1:
                    dp[i][j]=float(sum(nums[:i+1]))/(i+1)
                    continue
                if i+1<j:
                    dp[i][j]=0
                else:
                    # print(i,j)
                    for s in range(j-2,i):
                        dp[i][j]=max(dp[i][j],dp[s][j-1]+float(sum(nums[s+1:i+1]))/(i-s))
            print(dp[i])
        return dp[-1][-1]


nums =[4,1,7,5,6,2,3]
k =4
a=Solution()
print(a.largestSumOfAverages(nums,k))

