#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/3 12:38
# @Author  : sunaolin
# @File    : 84_1.py

# 为了方便，我们令 heights 为 hs。
# 最终矩形的高度必然取自某个 hs[i]，因此我们可以枚举最终矩形的高度来做。
# 问题转换为当使用某个 hs[i] 作为矩形高度时，该矩形所能取得的最大宽度为多少。
# 假设我们能够预处理出 l 和 r 数组，
# 其中 l[i] 代表位置 i 左边最近一个比其小的位置（初始值为 −1），
# r[i] 代表位置 i 右边最近一个比其小的位置（初始值为 n），那么 r[i]−l[i]−1 则是以 hs[i] 作为矩形高度时所能取得的最大宽度。
# 预处理 l 和 r 则是经典的「求最近一个比当前值大的位置」单调栈问题。


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        lst=[]
        rst=[]
        lb=[0]*len(heights)
        rb=[0]*len(heights)

        for i in range(len(heights)):
            while len(lst)>0 and heights[lst[-1]]>heights[i]:
                lst.pop()
            lb[i]=lst[-1] if len(lst)>0 else -1
            lst.append(i)

        for i in range(len(heights))[::-1]:
            while len(rst) > 0 and heights[rst[-1]] > heights[i]:
                rst.pop()
            lb[i] = rst[-1] if len(rst)>0 else len(heights)
            rst.append(i)
        res=0
        for i in range(len(heights)):
            res=max(res,heights[i]*(rb[i]-lb[i]-1))
        return res
