#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 10:34
# @Author  : sunaolin
# @File    : 250_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        num,_=self.dfs(root)
        return num






    def dfs(self,root):
        if root==None:
            return 0,float("inf")
        if root.left==None and root.right==None:
            return 1,root.val
        elif root.left==None:
            rn,rv=self.dfs(root.right)
            if root.val==rv:
                return rn+1,rv
            else:
                return rn,float("inf")
        elif root.left==None:
            ln,lv=self.dfs(root.left)
            if root.val==lv:
                return ln+1
            else:
                return ln,float("inf")
        else:
            ln, lv = self.dfs(root.left)
            rn, rv = self.dfs(root.right)
            if lv==rv==root.val:
                return ln+rn+1,root.val
            else:
                return ln+rn,float("inf")





