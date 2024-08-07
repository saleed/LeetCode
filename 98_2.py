#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 00:01
# @Author  : sunaolin
# @File    : 98_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res,_,_=self.dfs(root)
        return res


    def dfs(self,root):
        if root==None:
            return True,-float("inf"),float("inf")
        isl,lmax,lmin=self.dfs(root.left)
        isr,rmax,rmin=self.dfs(root.right)
        # return isl and isr and lmax < root.val < rmin, rmax,lmin  ###这样写是错的 要考虑lmax是-float("inf")的情况，会取不到有值节点
        return isl and isr and lmax<root.val<rmin,max(root.val,lmax,rmax),min(root.val,rmin,lmin)