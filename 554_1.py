#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/31 19:11
# @Author  : sunaolin
# @File    : 554_1.py


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        res=[[] for _ in range(len(wall))]
        bound={}

        for i in range(len(wall)):
            start=0
            for j in range(len(wall[i])):
                res.append([start,start+wall[i][j]])
                start+=wall[i][j]
                if start in bound:
                    bound[start]+=1
                else:
                    bound[start]=1
        maxv=0
        print(bound)
        del bound[sum(wall[0])]
        for k in bound:
            maxv=max(maxv,bound[k])
        return len(wall)-maxv

