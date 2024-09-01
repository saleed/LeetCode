#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/19 13:28
# @Author  : sunaolin
# @File    : 776.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitBST(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        if root==None:
            return None,None
        if root.val<=target:
            bns=self.splitBST(root.right,target)
            root.right=bns[0]
            return root,bns[1]
        else:
            bns=self.splitBST(root.left,target)
            root.left=bns[1]
            return bns[0],root
