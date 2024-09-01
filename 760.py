#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 14:02
# @Author  : sunaolin
# @File    : 760.py


class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]  and j not in res:
                    res.append(j)
                    break
        return res