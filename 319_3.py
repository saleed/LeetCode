#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 17:15
# @Author  : sunaolin
# @File    : 319_3.py


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        ele=[0]*(n+1)
        # for i in range(1,len(ele)):
        #     cnt=0
        #     for j in range(math.sqrt(i)+1):
        #         if i==j*j:
        #             cnt+=1
        #         elif i%j==0:
        #             cnt+=2
        #     ele[i]=cnt

        for i in range(1, n + 1):
            p = 1
            while p * i <= n:
                ele[p * i] += 1
                p += 1
        res=0
        for i in range(1,len(ele)):
            if ele[i]%2:
                res+=1
        return res



