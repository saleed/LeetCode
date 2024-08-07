#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/24 19:16
# @Author  : sunaolin
# @File    : 77_5.py


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        nums=[i+1 for i in range(n)]
        self.dfs(nums,0,[],res,k)
        return res




    def dfs(self,nums,i,tmp,res,left):
        print(tmp)
        if left==0:
            res.append(tmp[:])
            return
        if i>=len(nums):
            return

        self.dfs(nums,i+1,tmp,res,left)
        tmp.append(nums[i])
        self.dfs(nums,i+1,tmp,res,left-1)
        tmp.pop()


a=Solution()
print(a.combine(1,1))