#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 13:53
# @Author  : sunaolin
# @File    : 435_1.py


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        cnt=0
        new_itv=[]
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        for v in intervals:
            if len(new_itv)==0 or new_itv[-1][1]<=v[0]:
                new_itv.append(v)
            else:
                cnt += 1
                if v[1]>new_itv[-1][1]:
                    continue
                else:
                    new_itv.pop()
                    new_itv.append(v)


        return cnt