#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 10:09
# @Author  : sunaolin
# @File    : 400_1.py


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        numbit=1
        sumN=0
        while sumN<n:
            sumN+=numbit*pow(10,numbit-1)*9
            numbit+=1
        print(sumN)
        numbit-=1
        sumN-=pow(10,numbit-1)*9*numbit
        print("sumN",sumN)
        n-=sumN ##这里计算的是差值
        n-=1 #这里得到n的序号
        if numbit==1:
            d=1
        else:
            d=pow(10,numbit-1)

        d+=int(n/numbit)##这里得到是第几个数字
        print("d",d)
        n=n%numbit  ##余几位
        i=0
        while i<numbit-1-n:
            d=int(d/10)
            i+=1
        return d%10

a=Solution()
print(a.findNthDigit(11))