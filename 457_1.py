#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 19:29
# @Author  : sunaolin
# @File    : 457-1.py


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums)):
            j=(i+nums[i])%len(nums)
            cnt=1
            pre=nums[i]
            vis=set()
            while j!=i:
                cnt+=1
                if pre*nums[j]<0 or j in vis:
                    break
                pre=nums[j]
                vis.add(j)
                j=(j+nums[j])%len(nums)
            if j==i and cnt>1:
                return True
        return False

