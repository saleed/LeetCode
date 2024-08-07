#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/6 17:25
# @Author  : sunaolin
# @File    : 226_4.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        root.left=right
        root.right=left
        return root