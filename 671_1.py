#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 15:07
# @Author  : sunaolin
# @File    : 671——1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[float("inf"),float("inf")]
        self.dfs(root,res)
        if res[1]==float("inf") or res[1]==res[0]:
            return -1
        return res[1]


    def dfs(self,root,res):
        if root==None:
            return
        if root.val<res[0]:
            res[1]=res[0]
            res[0]=root.val
        elif root.val<res[1]:
            res[1]=root.val
        self.dfs(root.left,res)
        self.dfs(root.right,res)
