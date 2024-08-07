#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 19:17
# @Author  : sunaolin
# @File    : 179_3.py
from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res=[]
        for i in nums:
            res.append(str(i))
        # print res
        # res.sort(key=cmp_to_key(lambda x,y:x>y))  #the key sentence
        res.sort(reverse=True)
        print(res)
        rlt=""
        for i in res:
            if rlt=='0' and i=='0':
                continue
            rlt+=i
        return rlt

def compare(x,y):
    return x+y>y+x
# cmp_to_key
a=Solution()
Input= [3,30,34,5,9]
# Output: "9534330"
print(a.largestNumber(Input))



