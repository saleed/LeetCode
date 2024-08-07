#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 14:48
# @Author  : sunaolin
# @File    : 270_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ret,_=self.dfs(root,target)
        return ret

    def dfs(self,root,target):
        if root==None:
            return float("inf"),float("inf")
        diff=root.val-target
        if diff>0:
            lv,ldiff=self.dfs(root.left,target)
            if ldiff>diff:
                return root.val,diff
            else:
                return lv,ldiff
        else:
            rv,rdiff=self.dfs(root.right,target)
            if rdiff>diff:
                return root.val,diff
            else:
                return rv,rdiff



