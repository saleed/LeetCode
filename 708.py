#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/12 17:09
# @Author  : sunaolin
# @File    : 708.py


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head == None:
            q = Node(insertVal)
            q.next = q
            return q
        if head.next == head:
            q = Node(insertVal)
            q.next = head
            head.next = q
            return head
        print(head)

        dum = Node(-1)
        dum.next = head
        vis = set()
        minv = dum
        p = dum
        while p.next not in vis:
            if p.next.val < minv.next.val:
                minv = p
            vis.add(p.next)
            p = p.next

        n = 0
        p = minv
        while n < len(vis):
            if p.next.val < insertVal:
                p = p.next
                n += 1
            else:
                break

        if p.val==-1:
            n=0
            while n<len(vis):
                p=p.next
                n+=1

        q = Node(insertVal)
        q.next = p.next
        p.next = q
        return head







