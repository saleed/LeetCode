#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/21 14:52
# @Author  : sunaolin
# @File    : 144——5.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st=[]
        res=[]
        p=root
        while p!=None or len(st)>0:
            print(st)
            while p:
                if p.right:
                    st.append(p.right)
                res.append(p.val)
                p=p.val
            if len(st)>0:
                p=st.pop()
        return res