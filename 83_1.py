#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 12:43
# @Author  : sunaolin
# @File    : 83_.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dum=ListNode(float("inf"))
        dum.next=head
        p=dum
        while p:
            if p.next and p.next.val==p.val:
                q=p.next
                while q and q.val==p.val:
                    q=q.next
                p.next=q
            else:
                p=p.next
        return dum.next