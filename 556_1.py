#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/31 20:09
# @Author  : sunaolin
# @File    : 556_1.py

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """

        res=self.decode(n)
        id=-1
        for i in range(1,n)[::-1]:
            if res[i]<res[i-1]:
                continue
            else:
                id=i-1
                break
        if id==-1:
            return -1
        j=n-1
        while res[j]<res[id]:
            j-=1
        res[id],res[j]=res[j],res[id]
        p=id+1
        q=n-1
        while p<q:
            res[p],res[q]=res[q],res[p]
            p+=1
            q-=1
        return int("".join(res))




    def decode(self,n):##把n转成数组
        res=[]
        while n:
            res.append(n%10)
            n//=10
        return res[::-1]



