#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 16:38
# @Author  : sunaolin
# @File    : 589-1.py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """


        if root==None:
            return []
        res=[]
        res.append(root.val)
        for v in root.children:
            if v:
                res.extend(self.preorder(v))
        return  res



