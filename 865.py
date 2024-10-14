#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 00:42
# @Author  : sunaolin
# @File    : 865.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res=[(0,root)]
        self.dfs(root,0,res)
        return res[0][1]

    def dfs(self,root,depth,res):
        if root==None:
            return -1
        if root.left==None and root.right==None:
            if depth>res[0][0]:
                res[0]=(depth,root)
            return depth
        left=self.dfs(root.left,depth+1,res)
        right=self.dfs(root.right,depth+1,res)

        if left==right and left>=res[0][0]:
            res[0]=(left,root)
        return max(left,right)




