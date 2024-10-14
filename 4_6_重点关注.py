#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 12:50
# @Author  : sunaolin
# @File    : 4_6.py

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=(len(nums1)+len(nums2))
        if l%2==1:
            return self.findK(nums1,nums2,l/2+1)
        else:
            return (self.findK(nums1,nums2,l/2)+self.findK(nums1,nums2,l/2+1))/2.0


    def findK(self,nums1,nums2,K):
        if len(nums1)==0:
            return nums2[K-1]
        if len(nums2)==0:
            return nums1[K-1]
        if K==1:   ##这里必须提前设定K==1的情况，如果这里不截止，下一次的K一定为0，导致整个findK对K的定义出现歧义
            return min(nums1[0],nums2[0])

        p1=K/2-1  ##注意这里的下标
        p2=K/2-1
        if p1>=len(nums1):
            p1=len(nums1)-1
        if p2>=len(nums2):
            p2=len(nums2)-1

        if nums1[p1]>=nums2[p2]:
            return self.findK(nums1,nums2[p2+1:],K-(p2+1))
        else:
            return self.findK(nums1[p1+1:],nums2, K-(p1+1))