#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 14:06
# @Author  : sunaolin
# @File    : 215_5.py


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        self.quickSort(nums,0,len(nums)-1)
        print(nums)
        return nums[-k]

####基数排序必须保证所有的数字都大于0
    def radixSort(self,nums):
        sdict={}

        for i in range(10):
            base=pow(10,i)
            for v in nums:
                left=(nums/base)%10
                if left in sdict:
                    sdict[left].append(v)
                else:
                    sdict[left]=[v]
            nums=[b for a in sdict.values() for b in a]
        return nums

    def quickSort(self,nums,s,e):
        if s<=e:
            return
        else:
            p=s+1
            for i in range(s+1,e):
                if nums[i]<nums[s]:
                    nums[i],nums[p]=nums[p],nums[i]
                    p+=1
            nums[p-1],nums[s]=nums[s],nums[p-1]
            self.quickSort(nums,s,p-1)
            self.quickSort(nums,p+1,e)




