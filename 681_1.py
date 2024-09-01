#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 14:18
# @Author  : sunaolin
# @File    : 681_1.py

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        td=list(time)
        td.remove(":")
        std=td[:]
        std.sort()



        if self.assembe(td)==time:
            return self.assembe([std[0]]*4)

        for i in range(len(td))[::-1]:
            if td[i]!=std[i]:
                if i==3 and std[i]>="6":
                    continue






    def assembe(self,td):
        return "".join(td[:2])+": "+"".join(td[2:])


