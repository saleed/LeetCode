#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 13:58
# @Author  : sunaolin
# @File    : 253_1.py

class Solution:
    def minMeetingRooms(self, intervals):
        ### 上车下车
        up_down = []
        for start, end in intervals:
            up_down.append((start,  1))
            up_down.append((end, -1))
        print(up_down)
        up_down.sort()
        print(up_down)
        res = 0
        room = 0
        for _, n in up_down:
            room += n
            res = max(room, res)
        return res

a=Solution()
intervals =[[0,30],[5,10],[15,20]]
print(a.minMeetingRooms(intervals))