#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 10:16
# @Author  : sunaolin
# @File    : 666_1.py

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[0]

        self.dfs(nums,nums[0],0,res)
        return res[0]

    def dfs(self,nums,tmp,tmpsum,res):
        print(tmp)
        d,p,v=self.decode(tmp)
        l=self.findChild(nums,(d+1)*100+(2*p-1)*10)
        r=self.findChild(nums,(d+1)*100+(2*p)*10)
        print(l,r)
        if len(l)==0 and len(r)==0:
            res[0]+=(tmpsum+v)
            return
        if len(l)>0:
            for c in l:
                self.dfs(nums,c,tmpsum+v,res)
        if len(r)>0:
            for c in r:
                self.dfs(nums,c,tmpsum+v,res)


    def decode(self,i):
        res=[]
        i=int(i)
        while i:
            res.append(i%10)
            i=int(i/10)
        return res[::-1]
    def encode(self,d,p,val):
        return d*100+p*10+val

    def findChild(self,nums,prefix):
        res=[]
        for v in nums:
            if 0<=int(v)-prefix<=9:
                res.append(v)
        return res