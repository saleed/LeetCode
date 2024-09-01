#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 16:47
# @Author  : sunaolin
# @File    : 687.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0

        res=[0]
        self.dfs(root,res)
        return res[0]-1


    def dfs(self,root,res):
        if root==None:
            return 0,0,0


        lt,ll,lr=self.dfs(root.left,res)
        rt,rl,rr=self.dfs(root.right,res)
        l=0
        if root.left==None or root.left.val!=root.val:
            l=0
        else:
            l=max(ll,lr)
        r=0
        if root.right==None or root.right.val!=root.val:
            r=0
        else:
            r=max(rl,rr)

        if r+l+1>res[0]:
            res[0]=r+l+1
        print(root.val,1+r+l,l+1,r+1)

        return 1+r+l,l+1,r+1








