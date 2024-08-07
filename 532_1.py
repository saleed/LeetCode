#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 16:19
# @Author  : sunaolin
# @File    : 532_1.py


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0:
            return len(nums)-len(list(set(nums)))

        predict={}
        cnt=0
        for v in nums:
            if (v+k in predict or v-k in predict) and v not in predict:
                cnt+=1
            predict[v]=1
        return cnt
