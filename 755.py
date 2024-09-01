#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/17 15:47
# @Author  : sunaolin
# @File    : 755.py

class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """

        for _ in range(volume):
            left=-1
            i=k
            while i-1>=0:
                if heights[i]>heights[i-1]:
                    left=i-1
                    break
                elif heights[i]==heights[i-1]:
                    i-=1
                else:
                    break
            if left!=-1:
                heights[left]+=1
                # break
                continue  ##continue和break!!!!
            right = -1
            i=k
            while i +1<len(heights):
                if heights[i] > heights[i +1]:
                    right = i + 1
                    break
                elif heights[i] == heights[i + 1]:
                    i += 1
                else:
                    break
            if right != -1:
                heights[right] += 1
            else:
                heights[k]+=1
            print(heights)

        return heights



