d#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 10:57
# @Author  : sunaolin
# @File    : 201_5.py



class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        a=1
        res=0
        while a<=right:
            # print(a,right)
            T=a*2
            if right-left+1<=a:
                r=right%T
                l=left%T
                if l>=a and r>=a:
                    res+=a
            a=(a<<1)
            # print(a, right)
        return res

left=2
right=2
a=Solution()
print(a.rangeBitwiseAnd(left,right))