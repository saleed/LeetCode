#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/21 15:03
# @Author  : sunaolin
# @File    : 437_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        res=[0]
        pres=[]
        self.dfs(root,[],float("inf"),targetSum,res,pres)
        print(pres)
        return res[0]

    def dfs(self,root,path,tmp,target,res,pres):
        if tmp==target:
            res[0]+=1
            pres.append(path[:])
        if root!=None:
            self.dfs(root.left,[],0,target,res,pres)
            self.dfs(root.right,[],0,target,res,pres)
            path.append(root.val)
            if tmp==float("inf"):
                tmp=0
            self.dfs(root.left,path,tmp+root.val,target,res,pres)
            self.dfs(root.right,path,tmp+root.val,target,res,pres)
            path.pop()






