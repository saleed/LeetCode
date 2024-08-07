#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 15:19
# @Author  : sunaolin
# @File    : 314_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###因为是从上到下，所以不能用二叉树遍历的方法，只能层次遍历
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res={}
        l,r=self.dfs(root,0,res)
        lres=[]
        for k in range(l,r+1):
            lres.append(res[k])
        return lres




    def dfs(self,root,pos,res):
        if root==None:
            return float("inf"),-float("inf")
        if pos in res:
            res[pos].append(root.val)
        else:
            res[pos]=[root.val]
        ll,lr=self.dfs(root,pos-1,res)
        rl,rr=self.dfs(root,pos+1,res)
        return min(ll,rl,pos),max(lr,rr,pos)

