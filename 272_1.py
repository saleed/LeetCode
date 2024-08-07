#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/10 15:26
# @Author  : sunaolin
# @File    : 272_1.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res=[]
        self.inorder(root,res)


        id=-1
        mindiff=float("inf")
        for i in range(len(res)):
            if abs(res[i]-target)<mindiff:
                mindiff=abs(res[i]-target)
                id=i
        print(res,id)

        if k==0:
            return []
        topK=[res[id]]
        p=id-1
        q=id+1
        while p>=0 or q<len(res):
            pval=res[p] if p>=0 else float("inf")
            qval=res[q] if q<len(res) else float("inf")
            if abs(pval-target)<=abs(qval-target):
                topK.append(res[p])
                p-=1
            else:
                topK.append(res[q])
                q+=1

        return topK[:k]







    def inorder(self,root,res):
        if root==None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)


print(float("inf")-float("inf"))