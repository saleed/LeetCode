#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 13:50
# @Author  : sunaolin
# @File    : 230_4.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res=[]
        self.inorder(root,res)
        return res[k]

    def inorder(self,root,res):
        if root==None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)

