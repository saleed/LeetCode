#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 15:38
# @Author  : sunaolin
# @File    : 61_6.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return None

        l=1
        p=head
        while p.next:
            l+=1
            p=p.next
        k=k%l
        if k == 0: ###在这里判断
            return head
        i=1
        q=head
        while i<l-k:
            q=q.next
            i+=1
        newhead=q.next
        p.next=head
        q.next=None
        return newhead


