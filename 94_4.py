#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/21 14:08
# @Author  : sunaolin
# @File    : 94_4].py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """



        st=[]
        tmp=root
        res=[]
        while tmp!=None or len(st)>0:
            while tmp:
                st.append(tmp.left)
            top= st.pop()
            res.append(top.val)
            tmp=top.right

        return res





