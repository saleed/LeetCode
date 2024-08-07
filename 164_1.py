#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 12:39
# @Author  : sunaolin
# @File    : 164——1.py

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=self.radixSort(nums)

        res=0
        for i in range(len(nums)):
            res=max(res,nums[i]-nums[i-1])
        return res

    def radixSort(self,nums):
        for i in range(10):
            s=[[] for _ in range(10)]
            for v in nums:
                id=int(v/(10**i)%10)
                s[id].append(v)
            nums=[a for b in s for a in b]
        return nums