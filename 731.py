#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 13:50
# @Author  : sunaolin
# @File    : 731.py


class MyCalendarTwo(object):

    def __init__(self):
        self.calendar=[]
        self.oneintersec=[]






    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        for v in self.oneintersec:
            if end<v[0] or start>v[1]:
                continue
            else:
                return False
        for v in self.calendar:
            if end<v[0] or start>v[1]:
                continue
            else:
                self.oneintersec.append([max(v[0],start),min(v[1],end)])

        self.calendar.append([start,end])
        return True







# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)