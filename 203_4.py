#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/5 14:17
# @Author  : sunaolin
# @File    : 203_4.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum=ListNode(0)
        dum.next=head
        p=dum
        while p.next:
            if p.next.val==val:
                q=p.next
                p.next=q.next
                q.next=None
            else:
                p=p.next
        return dum.next

