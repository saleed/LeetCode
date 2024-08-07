#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 15:44
# @Author  : sunaolin
# @File    : 337_`.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res=self.dfs(root)
        return max(res)

    def dfs(self,root):
        if root==None:
            return 0,0
        l1,l2=self.dfs(root.left)
        r1,r2=self.dfs(root.right)

        return root.val+l2+r2,max(l1,l2)+max(r1,r2)

