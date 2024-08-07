#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/26 16:11
# @Author  : sunaolin
# @File    : 503_1.py


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ids=[-1]*len(nums)
        st=[]
        res=[-1]*len(nums)

        for i in range(2*len(nums)):
            while len(st)>0 and nums[st[-1]]<nums[i%(len(nums))]:
                ids[st.pop()]=nums[i%len(nums)]
            # print(i%len(nums))
            st.append(i%len(nums))
        return res



