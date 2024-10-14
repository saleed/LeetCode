#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/16 23:11
# @Author  : sunaolin
# @File    : 863.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        path=self.findpath(root,target)
        if k==0:
            return path
        for v in path:
            print(v.val)
        res=[]
        l=k
        for v in path[::-1]:
            if l>0:
                print(v.val,l)
                res+=self.findKchild(v,l,path)
                l-=1
        return res



    def findpath(self,root,target):
        if root==None:
            return []
        if root==target:
            return [root]

        left=self.findpath(root.left,target)
        right=self.findpath(root.right,target)
        # print(left,right)
        if len(left)>0:
            return [root]+left
        if len(right)>0:
            return [root]+right
        return []


    def findKchild(self,root,k,path):
        if root==None:
            return []
        if k==0:
            return [root.val]
        res=[]
        if root.left not in path:
            left=self.findKchild(root.left,k-1,path)
            res+=left
        if root.right not in path:
            right=self.findKchild(root.right,k-1,path)
            res+=right
        return res

