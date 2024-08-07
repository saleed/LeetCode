#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 18:32
# @Author  : sunaolin
# @File    : 426_1.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:
            return None
        head,tail=self.dfs(root)
        head.right=tail
        tail.left=head

        return tail


    def dfs(self,root):
        if root==None:
            return None,None
        lhead,ltail=self.dfs(root.left)
        rhead,rtail=self.dfs(root.right)
        root.left=lhead
        root.right=rtail
        if lhead:
            lhead.right=root
        if rtail:
            rtail.left=root

        head=rhead if rhead else root
        tail=ltail if ltail else root
        return head,tail


