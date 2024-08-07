#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 14:38
# @Author  : sunaolin
# @File    : 333_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        _,_,n,isbst=self.dfs(root,res)
        return res[0]



    def dfs(self,root,res):
        if root==None:
            return -float("inf"),float("inf"),0,True
        lmax,lmin,ln,lisBst=self.dfs(root.left,res)
        rmax,rmin,rn,risBst=self.dfs(root.right,res)

        if lmax<root.val<rmin and lisBst and risBst:
            res[0]=max(res[0],ln+rn+1)
            return max(root.val,rmax),min(root.val,lmin),ln+rn+1,True
        return max(lmax,root.val,rmax),min(rmin,lmin,root.val),ln+rn+1,False