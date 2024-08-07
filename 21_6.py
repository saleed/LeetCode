#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 11:03
# @Author  : sunaolin
# @File    : 21_6.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p=list1
        q=list2
        newhead=ListNode(0)
        r=newhead
        while p!=None or q!=None:
            pval=p.val if p else float("inf")
            qval=q.val if q else float("inf")
            if pval<qval:
                select=p
                p=p.next
            else:
                select=q
                q=q.next
            select.next=None
            r.next=select
            r=r.next
        return newhead.next


