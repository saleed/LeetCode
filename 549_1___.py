#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 15:27
# @Author  : sunaolin
# @File    : 549——1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]
        self.dfs(root,res)
        return res[0]

    def dfs(self,root,res):
        if root==None:
            return 0,0

        desc=1
        asc=1
        ldesc,lasc=self.dfs(root.left,res)
        rdesc,rasc=self.dfs(root.right,res)

        ##记录当前节点单侧的最大最小
        sdesc=1
        sasc=1

        if root.left:
            if root.left.val==root.val+1:
                asc+=lasc  ##从上往下增加
                sasc=max(sasc,1+lasc)
            if root.left.val==root.val-1:
                desc+=ldesc ##从上往下减少
                sdesc=max(sdesc,1+ldesc)
        if root.right:
            if root.right.val==root.val+1:
                desc+=ldesc
                sasc=max(sasc,1+rasc)
            if root.right.val==root.val-1:
                asc+=rdesc
                sdesc=max(sdesc,1+rdesc)


        res[0]=max(res[0],asc,desc)
        return sdesc,sasc






