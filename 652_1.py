#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/6 15:19
# @Author  : sunaolin
# @File    : 652_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        rdict={}
        self.dfs(root,rdict)
        res=[]
        for k in rdict:
            if len(rdict[k])>1:
                res.append(rdict[k][0])
        return res




    def dfs(self,root,rdict):
        if root==None:
            return "()"
        left=self.dfs(root.left,rdict)
        right=self.dfs(root.right,rdict)
        tmp="("+str(root.val)+left+right+")"
        if tmp in rdict:
            rdict[tmp].append(root)
        else:
            rdict[tmp]=[root]
        return tmp

