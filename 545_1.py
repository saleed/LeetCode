#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 11:12
# @Author  : sunaolin
# @File    : 545_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        print(root)
        if root==None:
            return None
        res=[]
        self.findLeaf(root,res)
        lb=self.findLeftBound(root.left)
        rb=self.findRightBound(root.right)
        # print(rb)
        res=lb+res+rb[::-1]
        if not(root.left==None and root.right==None):
            res=[root.val]+res

        return res


    def findLeaf(self,root,res):
        if root==None:
            return []
        if root.left==None and root.right==None:
            res.append(root.val)
            return

        self.findLeaf(root.left,res)
        self.findLeaf(root.right,res)

    def findLeftBound(self,root):
        res=[]
        while root and  (root.left or root.right):
            res.append(root.val)
            if root.left:
                root=root.left
            else:
                root=root.right
        return res

    def findRightBound(self, root):
        res = []
        print(root.val)
        while root and (root.left or root.right):
            res.append(root.val)
            # print(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        return res



