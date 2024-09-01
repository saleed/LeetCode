#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/11 14:36
# @Author  : sunaolin
# @File    : 701.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:
            return
        if root.val<=val
            if root.right==None:
                root.right=TreeNode(val)
            else:
                self.insertIntoBST(root.right,val)

        if root.val>val:
            if root.left==None:
                root.left=TreeNode(val)
            else:
                self.insertIntoBST(root.left,val)

