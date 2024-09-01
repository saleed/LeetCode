#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/12 19:21
# @Author  : sunaolin
# @File    : 713.py


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=0:
            return 0
        mul = 1
        p = 0
        res = 0
        for i in range(len(nums)):
            mul *= nums[i]
            # print(mul, k)
            while mul >= k  and p<=i: ##
                # print(mul, nums[p])
                mul = mul / nums[p]
                p += 1
            # print(i,p,(1 + i - p + 1) * (i - p + 1) / 2)
            if p<=i and mul<k:  ###这里一定加组限制条件
                res+=(i-p+1)
        return res

