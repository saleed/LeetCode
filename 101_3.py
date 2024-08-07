#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 10:52
# @Author  : sunaolin
# @File    : 101_3.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.symmetric(root.left,root.right)



    def symmetric(self,p,q):
        if p==None and q==None:
            return True
        if p and q:
            return p.val==q.val and self.symmetric(p.left,q.right) and self.symmetric(p.right,q.left)