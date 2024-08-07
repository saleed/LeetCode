#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 15:12
# @Author  : sunaolin
# @File    : 124_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res,_,_=self.dfs(root)
        return res


    def dfs(self,root):
        if root==None:
            return 0,0,0
        lmax,ll,lr=self.dfs(root.left)
        rmax,rl,rr=self.dfs(root.right)
        return max(lmax,rmax,root.val,ll+root.val,lr+root.val,rl+root.val,rr+root.val,ll+rr+root.val),max(root.val,root.val+ll,root.val+lr),max(root.val,root.val+rl,root.val+rr)


a=Solution()
