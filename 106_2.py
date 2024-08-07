#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 12:28
# @Author  : sunaolin
# @File    : 106_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder)==len(postorder)==0:
            return None
        id=-1
        for i in range(len(inorder)):
            if inorder[i]==postorder[-1]:
                id=i
                break
        root=TreeNode(postorder[-1])
        root.left=self.buildTree(inorder[:id],postorder[:id])
        root.right=self.buildTree(inorder[id+1:],postorder[id:-1])
        return root
