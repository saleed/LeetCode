#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 16:53
# @Author  : sunaolin
# @File    : 366_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        heightDict={}
        self.heightDfs(root,heightDict)

        keys=heightDict.keys()
        keys.sort()
        res=[]
        for k in keys:
            res.append(heightDict[keys[k]])
        return res

    def heightDfs(self,root,heightDict):
        if root==None:
            return 0
        left=self.heightDfs(root.left,heightDict)
        right=self.heightDfs(root.right,heightDict)

        h=max(left,right)+1
        if h in heightDict:
            heightDict[h].append(root.val)
        else:
            heightDict[h]=[root.val]
