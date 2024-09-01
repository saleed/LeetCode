#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 09:51
# @Author  : sunaolin
# @File    : 814.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        root0=self.dfs(root)
        if root0:
            return None
        return root



    def dfs(self,root):
        if root==None:
            return True
        l0=self.dfs(root.left)
        r0=self.dfs(root.right)
        if l0:
            root.left=None
        if r0:
            root.right=None
        if l0 and r0 and root.val==0:
            return True
        return False

