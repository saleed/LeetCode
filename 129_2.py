#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 17:10
# @Author  : sunaolin
# @File    : 129_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        tmp=0
        self.dfs(root,tmp,res)
        return res[0]
    def dfs(self,root,tmp,res):
        if root==None:
            return
        if root.left==None and root.right==None:
            res[0]+=tmp
            return
        self.dfs(root.left,tmp*10+root.val,res)
        self.dfs(root.right,tmp*10+root.val,res)


    def dfs2(self,root):
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [root.val]
        res=[]
        left=self.dfs2(root.left)
        right=self.dfs2(root.right)
        for v in left:
            res.append()
