#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/4 15:54
# @Author  : sunaolin
# @File    : 114_4.py


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if root==None:
            return None
        l=self.flatten(root.left)
        r=self.flatten(root.right)
        if l:
            rc=root.right
            root.right=root.left
            l.right=rc
            root.left=None
        if r:
            return r
        elif l:
            return l
        else:
            return root

