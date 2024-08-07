#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 10:17
# @Author  : sunaolin
# @File    : 99_2.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.inorder(root)
        return root

    def inorder(self,root):
        if root==None:
            return []
        res=[]
        left=self.inorder(root.left)
        right=self.inorder(root.right)
        if len(left)>0 and left[-1].val>root.val:
            left[-1].val,root.val=root.val,left[-1].val
        if len(right)>0 and root.val>right[0].val:
            root.val,right[0].val=right[0].val,root.val
        res.extend(left)
        res.append(root)
        res.extend(right)
        return res