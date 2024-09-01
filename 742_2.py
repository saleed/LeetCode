#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 09:43
# @Author  : sunaolin
# @File    : 742_2.py


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 22:27
# @Author  : sunaolin
# @File    : 742——1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

    ##res中存放叶子节点的深度，dfs返回k的深度

    ##思路是每次遇到一个节点，分左右查找k和叶子节点
    ##如果root非k 左右查找，返回叶子节点，的深度以及k距离当前root的深度
    def dfs(self,root,k,depth,ddict,res):
        if root==None:
            return -1,None
        kdepth=-1
        if root.val==k:
            kdepth=depth
        if root.left==None and root.right==None:
            ddict[root]=depth
            return kdepth

        kdl, left = self.dfs(root.left, k, depth + 1, res)
        kdr, right = self.dfs(root.right, k, depth + 1, res)
        if kdl!=-1:
            for v in right:




