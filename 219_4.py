#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 16:41
# @Author  : sunaolin
# @File    : 219——4.py


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        pos=dict()

        for i in range(len(nums)):
            if nums[i] in pos:
                if i-pos[nums[i]]<=k:
                    return True
            pos[nums[i]]=i
        return False


