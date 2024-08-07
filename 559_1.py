#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 15:39
# @Author  : sunaolin
# @File    : 559_1.py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        ##被题目舞蹈了，题目中层序遍历的表示方式是有歧义的，不是数组形式的层序结果
        [1, null, 3, 2, 4, null, 5, 6]