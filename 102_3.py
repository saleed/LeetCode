#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 10:55
# @Author  : sunaolin
# @File    : 102_3.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        res=[]
        tmp=[root]

        while len(tmp)>0:
            ntmp=[]
            tmpres=[]
            for p in tmp:
                tmpres.append(p.val)
                if p.left:
                    ntmp.append(p.left)
                if p.right:
                    ntmp.append(p.right)
            tmp=ntmp
            res.append(tmpres)
        return res
