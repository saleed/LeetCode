#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 21:00
# @Author  : sunaolin
# @File    : 147——3.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dum=ListNode(-float("inf"))
        q=head
        while q:
            p=dum
            while p.next!=None and p.next.val<q.val:
                p=p.next

            nq=q.next

            q.next=None
            np=p.next
            p.next=q
            q.next=np
            q=nq
        return dum.next





