#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/17 18:19
# @Author  : sunaolin
# @File    : 872.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1==root2==None:
            return True

        leaf1=[]
        self.preorder(root1,leaf1)
        leaf2=[]
        self.preorder(root2,leaf2)
        print(leaf1,leaf2)
        if len(leaf2)==len(leaf1):
            for i in range(len(leaf1)):
                if leaf2[i]!=leaf1[i]:
                    return False
            return True
        return False

    def preorder(self,root,res):
        if root==None:
            return
        if root.left==None and root.right==None:
            res.append(root.val)

        self.preorder(root.left,res)
        self.preorder(root.right,res)



