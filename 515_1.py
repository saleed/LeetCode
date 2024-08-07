#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 16:37
# @Author  : sunaolin
# @File    : 515_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        level=[root]
        res=[]
        while len(level)>0:
            tmp=[]
            maxv=-float("inf")
            for v in level:
                if v.val>maxv:
                    maxv=v.val
                if v.left!=None:
                    tmp.append(v.left)
                if v.right!=None:
                    tmp.append(v.right)
            res.append(maxv)
            level=tmp
        return res



