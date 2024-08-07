#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 16:38
# @Author  : sunaolin
# @File    : 536_1.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """

        if len(s)==0:
            return None

        i=0
        while i<len(s) and s[i]!="(":
            i+=1
        print(s[:i])
        root=TreeNode(int(s[:i]))
        st=1
        j=i+1
        while j<len(s) and st>0:
            if s[j]=="(":
                st+=1
            elif s[j]==")":
                st-=1
            j+=1
        root.left=self.str2tree(s[i+1:j-1])
        root.right=self.str2tree(s[j+1:-1])
        return root


