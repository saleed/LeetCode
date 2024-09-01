#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 22:27
# @Author  : sunaolin
# @File    : 742——1.py

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res=[]
        self.dfs(root,k,0,0,res)
        kdep=0
        for v in res:
            if v[0]==-1:
                kdep=v[1]
                break

        mind=float("inf")
        minN=None
        for v in res:
            if v[0]==0 and kdep+v[1]<mind:
                mind=kdep+v[1]
                minN=v
            if v[0]==1 and v[1]-kdep<mind:
                mind=v[1]-kdep
                minN=v
        return minN[2]

    ##res中存放叶子节点到目标节点公共父节点的深度
    ##如果公共父节点是k
    ##
    def dfs(self,root,k,depth,meetk,res):
        if root==None:
            return

        if root.val==k:
            res.append([-1,depth,0])###存放特殊标志-1 表示找到根节点的深度
            meetk=1
        if root.left==None and root.right==None:
            res.append([meetk,depth,root])

        self.dfs(root.left, k, depth + 1, meetk, res)
        self.dfs(root.right, k, depth + 1, meetk, res)

