#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 13:10
# @Author  : sunaolin
# @File    : 42_4.py


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        st=[]
        res=0
        for i in range(len(height)):
            while len(st)>0 and height[st[-1]]<height[i]:
                j=st.pop()
                if len(st)==0:
                    break
                top=st[-1]
                minh=min(height[top],height[i])
                area=(i-top-1)*(minh-height[j])
                res+=area
            st.append(i)
        return res