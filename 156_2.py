#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 14:32
# @Author  : sunaolin
# @File    : 156_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        newroot=root
        while newroot.left:
            newroot=newroot.left
        self.dfs(root,None,None)
        return newroot

    def dfs(self,root,father,bro):
        if root==None:
            return
        left=root.left
        right=root.right
        root.left=bro
        root.right=father
        self.dfs(left,root,right)
        # self.dfs(right,None,None)


