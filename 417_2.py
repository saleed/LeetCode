#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 12:00
# @Author  : sunaolin
# @File    : 417_1.py



##用bfs比用dfs好很多

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ##reach表示之前已经算出可以抵达大西洋和太平洋的节点
        ##动态规划也可以解决，但是怎么解决相邻高度相同的问题
        ##417和417_1都忽略了上面的情况？？？？ 只有bfs不会遇到这种问题






