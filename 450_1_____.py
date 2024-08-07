#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 15:08
# @Author  : sunaolin
# @File    : 450_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        dum=TreeNode(float("inf"))
        dum.left=root
        self.search(dum,root,0,key)
        return root

    def search(self,fa,root,lr,key):
        if root==None:
            return
        if root.val==key:
            ##先判断有没有右子树
            if root.right==None:
                if lr==0:
                    fa.left=root.left
                else:
                    fa.right=root.left
                return
            else: ##右子树找最大的
                tmpfather=None
                tmp=root.right
                while tmp.left!=None:
                    tmpfather=tmp
                    tmp=tmp.left
                if tmpfather!=None:
                    tmpfather.left=tmp.right

            if lr==0:

                fa.left=tmp
            else:
                tmp.right=fa.right
                fa.right=tmp
        else:
            self.search(root,root.left,0,key)
            self.search(root,root.right,1,key)



