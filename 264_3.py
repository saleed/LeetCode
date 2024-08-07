#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 15:51
# @Author  : sunaolin
# @File    : 264_3.py


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ptr=[0,0,0]  ##含义是丑数序列中能够乘以2,3,5的最小索引
        mul=[2,3,5]
        res=[1]

        while len(res)<n:
            sel=-1
            minv=float("inf")
            for i in range(3):
                if res[ptr[i]]*mul[i]<minv:
                    sel=i
                    minv=min(minv,res[ptr[i]]*mul[i])
            ptr[sel]+=1
            if minv == res[-1]: ##可能重复 2*3 3*2
                continue
            # print(res)
            res.append(minv)


        return res[-1]


