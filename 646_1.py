#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 14:26
# @Author  : sunaolin
# @File    : 646_1.py

##怎么证明

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        pairs.sort(key=lambda x:x[0])
        print(pairs)
        top=pairs[0]
        cnt=0

        for i in range(1,len(pairs)):
            if pairs[i][0]>top[1]:

                cnt+=1
                top=pairs[i]
            else:
                if pairs[i][1]<top[1]:
                    top=pairs[i]
        return cnt