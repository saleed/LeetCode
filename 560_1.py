#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 09:45
# @Author  : sunaolin
# @File    : 560_1.py


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum=0
        psdict={}
        res=0

        for v in nums:
            presum+=v
            if presum-k in psdict:
                res+=psdict[presum-k]

            if presum in psdict:
                psdict[presum]+=1
            else:
                psdict[presum]=1
        return res