#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 19:12
# @Author  : sunaolin
# @File    : 538_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root,0)
        return root


##每一个节点，需要获得父亲大于等于该节点的值，以及右子树的节点值和
    def dfs(self,root,f):
        if root==None:
            return 0
        rv=0
        if root.right!=None:
            rv+=self.dfs(root.right,f)
        lv=self.dfs(root.left,rv+f+root.val)
        tmp=root.val
        root.val=rv+f+root.val
        return tmp+rv+lv




