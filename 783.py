#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 15:21
# @Author  : sunaolin
# @File    : 783.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[float("inf")]
        self.dfs(root,res)
        return res[0]


    def dfs(self,root,res):
        if root==None:
            return -float("inf"),float("inf")
        lmax,lmin=self.dfs(root.left,res)
        rmax,rmin=self.dfs(root.right,res)
        res[0]=min(res,abs(root.val-lmax),abs(root.val-rmin))
        return max(rmax,root.val),min(lmin,root.val)