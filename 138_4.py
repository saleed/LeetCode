#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 19:02
# @Author  : sunaolin
# @File    : 138_4.py


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """


        p=head

        ptrDict={}
        dum=Node(0)
        q=dum
        while p:
            q.next=Node(p.val)
            q=q.next
            ptrDict[p]=q
            p=p.next

        p=head
        q=dum.next
        while p:
            if p.random:
                q.random=ptrDict[p.random]
            p=p.next
            q=q.next
        return dum.next


