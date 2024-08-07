#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 11:31
# @Author  : sunaolin
# @File    : 606_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        return self.dfs(root)[1:-1]



    def dfs(self,root):
        if root == None:
            return "()"
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        if left=="()" and right=="()":
            left=""
            right=""
        elif right=="()":
            right=""


        return "("+str(root.val)+left+right+")"


