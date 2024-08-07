#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 15:02
# @Author  : sunaolin
# @File    : 114——3.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        return root



    def dfs(self,root):
        if root==None:
            return None,None
        lhead,ltail=self.dfs(root.left)
        rhead,rtail=self.dfs(root.right)
        if lhead!=None:
            root.left=None
            root.right=lhead
            if rhead:
                ltail.right=rhead
                return root,rtail
            else:
                return root,ltail
        else:
            if rhead:
                return root,rtail
            else:
                return root,root





