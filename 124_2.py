#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/4 17:48
# @Author  : sunaolin
# @File    : 124——2.py


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res,_=self.dfs(root)
        return res



    def dfs(self,root):
        if root==None:
            return -float("inf"),-float("inf")

        lmax,lhmax=self.dfs(root.left)
        rmax,rhmax=self.dfs(root.right)

        tmphalfmax=root.val+max(0,lhmax,rhmax,lhmax+rhmax)

        return max(lmax,rmax,tmphalfmax),tmphalfmax