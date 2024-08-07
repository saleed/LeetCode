#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/6 15:34
# @Author  : sunaolin
# @File    : 653.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        self.preorder(root, res)
        p = 0
        q = len(res) - 1
        while p < q:
            s = res[p] + res[q]
            if s == k:
                return True
            elif s < k:
                p += 1
            else:
                q -= 1
        return False

    def preorder(self, root, res):
        if root == None:
            return
        self.preorder(root.left, res)
        res.append(root.val)
        self.preorder(root.right, res)

