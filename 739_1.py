#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 16:26
# @Author  : sunaolin
# @File    : 739_1.py


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        st=[]
        res=[0]*len(temperatures)

        for i in range(len(temperatures)):

            while len(st)>0 and temperatures[st[-1]]<temperatures[i]:
                pre=st.pop()
                res[pre]=i-pre

            st.append(i)
        return res



