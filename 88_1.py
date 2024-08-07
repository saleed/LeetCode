#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 13:02
# @Author  : sunaolin
# @File    : 88_1.py


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        res=[]
        p=0
        q=0

        while p<m or q<n:
            pval=float("inf") if p==m else nums1[p]
            qval=float("inf") if q==n else nums2[q]
            if pval<qval:
                res.append(pval)
                p+=1
            else:
                res.append(qval)
                q+=1
        for i in range(len(nums1)):
             nums1[i]=res[i]
