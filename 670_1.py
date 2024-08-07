#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 13:46
# @Author  : sunaolin
# @File    : 670.py

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        numsort=list(str(num))
        numsort.sort(reverse=True)
        num=list(str(num))
        print(numsort)

        for i in range(len(numsort)):
            if num[i]!=numsort[i]:
                if i<len(numsort)-1:
                    id=num[::-1].index(numsort[i]) ###注意这里一定是从后往前找！！！
                    num[len(num)-1-id],num[i]=num[i],num[len(num)-1-id]
                    break
        return int("".join(num))









