#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 14:21
# @Author  : sunaolin
# @File    : 235_4.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res=[None]
        self.findPQ(root,p,q,res)
        return res[0]

    def findPQ(self,root,p,q,res):
        if res[0]!=None:
            return 0,0
        if root==None:
            return 0,0
        findP=0
        findQ=0

        lfindP,lfindQ=self.findPQ(root.left,p,q,res)
        rfindP,rfindQ=self.findPQ(root.right,p,q,res)
        if root.val==p.val:
            findP=1
            if lfindQ or rfindQ:
                res[0]=root
        elif root.val==q.val:
            findQ=1
            if lfindP or rfindP:
                res[0]=root
        else:
            if (lfindP and rfindQ) or (lfindQ and rfindP):
                res[0]=root
        return max(findP,lfindP,rfindP),max(findQ,lfindQ,rfindQ)

