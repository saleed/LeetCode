#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/21 15:00
# @Author  : sunaolin
# @File    : 145_4.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        st=[]
        prev=None
        p=root
        res=[]

        while p!=None and len(st)>0:
            while p:
                st.append(p)
                p=p.left

            p=st.pop()
            if p.right==None or prev==p: ##
                res.append(p.val)
                prev=p
                p=None
            else:
                st.append(p)
                p=p.right
        return res
