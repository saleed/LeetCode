#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 18:43
# @Author  : sunaolin
# @File    : 33_3.py


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        p=0
        q=len(nums)-1
        while p<=q: ###当跳出条件为p<=q时候，更新边界要为q=mid-1 否则当p==q时候，mid为p或者q，target如果比nums[mid]小的话，q=mid无法跳出循环
            mid=(p+q)/2
            if nums[mid]==target:
                return mid
            if nums[p]<=nums[mid]:  ##一定要是<= 如果mid=p的情况
                if  nums[p]<=target<nums[mid]:##target已经判断过<nums[mid] 需要判断是否<=nums[p] 而不是<nums[p]
                    q=mid-1
                else:
                    p=mid+1
            else:
                if nums[mid] < target <= nums[q]:
                    p=mid+1
                else:
                    q=mid-1
        return -1



