#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 16:22
# @Author  : sunaolin
# @File    : 513_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return None
        res=[[root.val,0,0]]
        self.dfs(root,res,0,0)
        return res[0][0]


    def dfs(self,root,res,pos,dep):
        if root==None:
            return
        if res[0][1]<dep or (res[0][1]==dep and res[0][2]>pos):
            res[0][0]=root.val
            res[0][1]=dep
            res[0][2]=pos
            print(res)

        self.dfs(root.left,res,pos-1,dep+1)
        self.dfs(root.right,res,pos+1,dep+1)


