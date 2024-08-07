#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 11:01
# @Author  : sunaolin
# @File    : 526_1.py


class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[0]
        nums=[i+1 for i in range(n)]
        self.dfs(nums,1,res)
        return res[0]


    def dfs(self,nums,i,res):
        if len(nums)==0:
            res[0]+=1
            return
        for v in nums:
            if i%v==0 or v%i==0:
                nnums=nums[:]
                nnums.remove(v)
                self.dfs(nnums,i+1,res)

