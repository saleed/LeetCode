#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 10:22
# @Author  : sunaolin
# @File    : 563_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _,p=self.dfs(root)
        return p

    def dfs(self,root):
        if root==None:
            return 0,0
        lsum,lp=self.findTilt(root.left)
        rsum,rp=self.findTilt(root.right)

        return lsum+rsum+root.val,lp+rp+abs(lsum-rsum)