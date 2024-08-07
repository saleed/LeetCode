#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 16:35
# @Author  : sunaolin
# @File    : 452——1.py


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        right=-float("inf")
        cnt=0
        for v in points:
            if v[0]>right:
                cnt+=1
                right=v[1]
            else:
                right=min(right,v[1])
        return cnt
