#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 10:01
# @Author  : sunaolin
# @File    : 201_6.py



class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        i=1
        res=0
        while right>=pow(2,i-1):
            T=pow(2,i)
            # print(T)
            # print(right-left+1, right%T,left%T)
            if right-left+1<=T/2 and T/2<=right%T  and T/2<=left%T:
                res=(1<<(i-1))|res
            i+=1
        return res


