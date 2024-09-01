#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 13:38
# @Author  : sunaolin
# @File    : 729_1.py


class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        id = -1
        for i in range(len(self.calendar)):
            if end <= self.calendar[i][0]:  ##这里和题目不太符合
                id = i
                break
            elif start >= self.calendar[i][1]:
                continue
            else:
                return False
        if id == -1:
            self.calendar.append([start, end])
        else:
            self.calendar = self.calendar[:id] + [[start, end]] + self.calendar[id:]

        # print(self.calendar)

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)