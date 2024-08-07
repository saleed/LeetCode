#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/6 17:33
# @Author  : sunaolin
# @File    : 662_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ##满二叉树，节点编号从1开始，当前节点n 左子树2n 右子树2n+1
        tmp=[(root,1)]
        maxl=0
        while len(tmp)>0:
            ntmp=[]
            left=float("inf") ###这里的右边界初始化错误
            right=0
            for v in tmp:
                if v[0].left:
                    ntmp.append((v[0].left,2*v[1]))
                if v[0].right:
                    ntmp.append((v[0].right,2*v[1]+1))
                left=min(left,v[1])
                right=max(right,v[1])
            # print(tmp,left,right)
            tmp=ntmp

            maxl=max(maxl,right-left+1)
        return maxl
