#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 11:31
# @Author  : sunaolin
# @File    : 116_3.py


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:
            return root
        tmp_tail=None
        if root.left:
            tmp_tail=root.left
            root.left.next=root.right
        if root.right:
            tmp_tail=root.right
        next_head=None
        p=root.next
        while p:
            if p.left:
                next_head=p.left
                break
            elif p.right:
                next_head=p.right
                break
            else:
                p=p.next
        if tmp_tail:
            tmp_tail.next=next_head
        self.connect(root.left)
        self.connect(root.right)
        return root




