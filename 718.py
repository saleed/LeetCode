#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 14:09
# @Author  : sunaolin
# @File    : 718.py


class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ##和LCS有明显不同，这里的子数组的长度必须连续的
        dp=[[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        maxl=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if i==0 or j==0:
                    dp[i][j]=1 if nums1[i]==nums2[j] else 0
                else:
                    dp[i][j]=dp[i-1][j-1]+1 if nums1[i]==nums2[j] else 0
            maxl=max(maxl,dp[i][j])
        return maxl

