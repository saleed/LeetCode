#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 19:05
# @Author  : sunaolin
# @File    : 45_3.py


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        step=1

        while True:
            np=p
            maxd=-float("inf")
            for d in range(nums[p]+1):
                if p+d>=len(nums):
                    return step
                elif p+d+nums[p+d]>maxd:
                    maxd=p+d+nums[p+d]
                    np=p+d

            p=np
            if p<len(nums):
                step+=1
            else:
                break
        return step


