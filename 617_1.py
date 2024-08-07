#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 13:35
# @Author  : sunaolin
# @File    : 617_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1==None and root2==None:
            return None
        v1=0 if root1==None else root1.val
        v2=0 if root2==None else root2.val
        root=TreeNode(v1+v2)
        l1=root1.left if root1 else None
        l2=root2.left if root2 else None
        r1=root1.right if root2 else None
        r2=root2.right if root2 else None
        root.left=self.mergeTrees(l1,l2)
        root.right=self.mergeTrees(r1,r2)
        return root
