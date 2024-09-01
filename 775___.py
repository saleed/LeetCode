#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 15:40
# @Author  : sunaolin
# @File    : 775.py



class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ##一个局部倒置一定是一个全局倒置，因此要判断数组中局部倒置的数量是否与全局倒置的数量相等，只需要检查有没有非局部倒置就可以了。

        premax=-float("inf")
        i=0
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                if nums[i+1]<premax:
                    return False
                i+=2
            else:
                if nums[i]<premax:
                    return False
                i+=1
            premax = max(premax, nums[i])



        return True


