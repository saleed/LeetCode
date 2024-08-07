#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 14:09
# @Author  : sunaolin
# @File    : 508_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        freq={}
        self.dfs(root,freq)
        print(freq)
        maxcnt=max(freq.values())
        res=[]
        for k in freq:
            if freq[k]==maxcnt:
                res.append(k)
        return res


    def dfs(self,root,res):
        if root==None:
            return float("inf")
        left=self.dfs(root.left,res)
        right=self.dfs(root.right,res)

        sumv=root.val
        if left!=float("inf"):
            sumv+=left
        if right!=float("inf"):
            sumv+=right

        if sumv in res:
            res[sumv]+=1
        else:
            res[sumv]=1
        return sumv
