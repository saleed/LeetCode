#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 14:23
# @Author  : sunaolin
# @File    : 24_5.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dum=ListNode(0)
        dum.next=head
        p=dum
        q=p.next
        r=q.next if q else None
        while r:
            s=r.next
            p.next=r
            r.next=q
            q.next=s
            p=q
            q=p.next
            r=q.next if q else None
        return dum.next