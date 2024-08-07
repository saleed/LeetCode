#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 21:08
# @Author  : sunaolin
# @File    : 95_3.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        nums=[i+1 for i in range(n)]


        return self.dfs(nums)

    def dfs(self,nums):
        res=[]
        if len(nums)==0:
            return [None]
        for i in range(len(nums)):
            left=self.dfs(nums[:i])
            right=self.dfs(nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(nums[i])
                    root.left=l
                    root.right=r
                    res.append(root)
        return res


