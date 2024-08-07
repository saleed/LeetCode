#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 12:18
# @Author  : sunaolin
# @File    : 105_3.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==len(inorder)==0:
            return None
        root=TreeNode(preorder[0])
        id=-1
        for i in range(len(inorder)):
            if inorder[i]==root.val:
                id=i
        root.left=self.buildTree(preorder[1:id+1],inorder[:id])
        root.right=self.buildTree(preorder[id+1:],inorder[id+1:])
        return root