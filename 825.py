#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 17:45
# @Author  : sunaolin
# @File    : 825.py







class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res=0
        for x in range(len(ages)):
            for y in range(x):
                if (ages[y] <= 0.5 * ages[x] + 7) or (ages[y] > ages[x]) or (ages[y] > 100 and  ages[x] < 100):
                    res+=1
        return res

