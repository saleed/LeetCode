#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 09:14
# @Author  : sunaolin
# @File    : 665_1.py


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        cnt=0
        pre=nums[0]

        ##首先找到第一个逆序数，然后找到两个逆序数较小的一个且比之前数都大的数  保留该数
        for i in range(1,len(nums)):
            if nums[i]>=pre:
                pre=nums[i]
                continue
            ppre=nums[i-2] if i>=2 else -float("inf")
            if nums[i]>=ppre: ##逆序数中的较小
                pre=nums[i]
            else:
                pre=nums[i-1]
            cnt += 1
            if cnt>1:
                return False
        return True



