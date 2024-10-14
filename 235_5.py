#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 20:46
# @Author  : sunaolin
# @File    : 235_5.py


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root,p,q)





    def dfs(self,root,p,q):
        if root==None:
            return None
        if (root.val==p or root.val==q) and (self.dfs(root.left,p,q)!=None or self.dfs(root.right,p,q)!=None):
            return root
        else:
            lret=self.dfs(root.left,p,q)
            rret=self.dfs(root.right,p,q)
            if lret and rret:
                return root

            if lret:
                return lret
            if rret:
                return rret

