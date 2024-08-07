#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/15 10:26
# @Author  : sunaolin
# @File    : 328_3.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # ods=ListNode(0)
        even=ListNode(0)
        # ods.next=head
        p=head
        q=even
        while p.next:
            s=p.next
            p.next=p.next.next
            s.next=None
            q.next=s
            q=s

        p.next=even.next
        return head

