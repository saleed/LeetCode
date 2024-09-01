#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 16:47
# @Author  : sunaolin
# @File    : 823.py


class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        dp=[1]*len(arr)
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i]%arr[j]==0:
                    dp[i]+=dp[j]
        return sum(dp)
