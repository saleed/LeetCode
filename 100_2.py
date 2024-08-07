#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 10:45
# @Author  : sunaolin
# @File    : 100_2.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        if p!=None and q!=None:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False

