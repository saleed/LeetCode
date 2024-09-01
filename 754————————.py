#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 17:03
# @Author  : sunaolin
# @File    : 754.py



class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """

        sumv=0
        i=1
        target=abs(target)
        while sumv<target:
            sumv+=i
            i+=1
        if (sumv-target)%2==0:
            return i-1
        else:
            return i +(i+1)%2

        ## sumv-target如果是偶数
        ## 可以直接改变(sumv-target)/2的符号
        ## 