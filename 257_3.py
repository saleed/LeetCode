#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 15:17
# @Author  : sunaolin
# @File    : 257_3.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root==None:
            return []

        lv=self.binaryTreePaths(root.left)
        rv=self.binaryTreePaths(root.right)

        res=[]
        for v in lv:
            res.append(str(root.val)+"->"+v)
        for v in rv:
            res.append(str(root.val)+"->"+v)
        if len(res)==0:
            res=[str(root.val)]
        return res