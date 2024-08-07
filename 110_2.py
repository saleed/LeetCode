#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 12:52
# @Author  : sunaolin
# @File    : 110_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _,isb=self.dfs(root)
        return isb


    def dfs(self,root):
        if root==None:
            return 0,True
        ld,lisb=self.dfs(root.left)
        rd,risb=self.dfs(root.right)
        return max(ld,rd)+1,lisb and risb

