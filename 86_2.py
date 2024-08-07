#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 12:51
# @Author  : sunaolin
# @File    : 86_2.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        lesshead=ListNode(0)
        r=lesshead
        morehead=ListNode(0)
        morehead.next=head
        p=morehead
        while p.next:
            if p.next.val<x:
                q=p.next
                p.next=q.next
                q.next=None
                r.next=q
                r=r.next
            else:
                p=p.next
        r.next=morehead.next
        return lesshead.next
