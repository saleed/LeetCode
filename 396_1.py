#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 19:33
# @Author  : sunaolin
# @File    : 396_1.py


class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumN = sum(nums)
        head = 0
        tail = len(nums) - 1
        i = 0
        tmpres = 0
        for i in range(len(nums)):
            tmpres += i * nums[i]
        res = tmpres
        i = 0
        print(res)
        while i < len(nums):
            tmpres = tmpres + (sumN) - (len(nums)) * nums[tail]

            res = max(res, tmpres)
            print(i, tmpres)

            head = (head + 1) % len(nums)
            tail = (tail + 1) % len(nums)
            i += 1
        return res
