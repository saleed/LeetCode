#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/11 13:28
# @Author  : sunaolin
# @File    : 697.py


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        bound={}

        freq={}
        maxfreq=0
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            maxfreq=max(maxfreq,freq[nums[i]])

            if nums[i] in bound:
                bound[nums[i]][1]=i
            else:
                bound[nums[i]]=[i,i]
        minl=len(nums)
        for k in freq:
            if freq[k]==maxfreq:
                minl=min(minl,bound[k][1]-bound[k][0])
        return minl






