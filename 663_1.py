#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 00:25
# @Author  : sunaolin
# @File    : 663_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sumv = self.TreeSum(root)
        if sumv % 2 == 1:
            return False

        _, lret = self.SumTarget(root.left, sumv / 2)
        _, rret= self.SumTarget(root.right,sumv/2)
        return lret or rret

    def TreeSum(self, root):
        if root == None:
            return 0
        return root.val + self.TreeSum(root.left) + self.TreeSum(root.right)

    def SumTarget(self, root, target):
        if root == None:
            return 0, False
        lsum, lfind = self.SumTarget(root.left, target)
        if lfind:
            return 0, True
        rsum, rfind = self.SumTarget(root.right, target)
        if rfind:
            return 0, True
        sumv = root.val + lsum + rsum
        return sumv, sumv == target


