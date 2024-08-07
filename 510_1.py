#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 14:51
# @Author  : sunaolin
# @File    : 510_1.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right!=None:
            p=node.right
            while p.left!=None:
                p=p.left
            return p
        else:
            p=node.parent
            while p and p.val<node.val:
                p=p.parent
            return p


