#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/14 20:16
# @Author  : sunaolin
# @File    : 230_5.py


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """


        _,ret=self.dfs(root,k)
        return ret
    def dfs(self,root,k):
        if root==None:
            return 0,None
        lnum,lret=self.dfs(root.left,k)
        if lret!=None:
            return 0,lret
        if lnum==k-1:
            return 0,root  ##注意这里的返回节点数是不需要的，如果lret非空，则目标节点已经找到，
        rnum,rret=self.dfs(root.right,k-lnum-1)
        return lnum+rnum+1,rret