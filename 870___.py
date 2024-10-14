#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 17:37
# @Author  : sunaolin
# @File    : 870.py


class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        id1=[i for i in range(len(nums1))]
        id2=[i for i in range(len(nums2))]


        id1.sort(key=lambda x:nums1[x])
        id2.sort(key=lambda x:nums2[x])
        print(id1,id2)

        res=[]
        left=0
        for i in range(len(nums1)):
            if nums1[id1[i]]>nums2[id2[left]]:
                left+=1
            res.append(nums1[id1[i]])
        return res
