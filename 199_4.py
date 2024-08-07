#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 20:18
# @Author  : sunaolin
# @File    : 199_4.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        left=self.rightSideView(root.left)
        right=self.rightSideView(root.right)
        res=[root]+left
        if len(left)>len(right):
            return res+left[len(right):]
        return res

