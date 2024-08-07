#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 15:45
# @Author  : sunaolin
# @File    : 404_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,1)


    def dfs(self,root,lr):
        res=0
        if root==None:
            return 0
        if lr==0 and root.left==None and root.right==None:
            res+=root.val
            return res
        else:
            lv=self.dfs(root.left,0)
            rv=self.dfs(root.right,1)
            return lv+rv






