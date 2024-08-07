#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 20:18
# @Author  : sunaolin
# @File    : 92-4.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dum=ListNode(0)
        dum.next=head
        l=1
        p=dum
        while l<left and p:
            p=p.next
            l+=1
        if p:
            lefthead=p
        else:
            return head

        while l<=right and p:###这里必须找到第right+1个节点
            p=p.next
            l+=1

        righthead=p.next if p else None
        if p:
            p.next=None

        print(lefthead)
        ln,rb=self.reverse(lefthead.next)
        lefthead.next=ln
        if rb:
            rb.next=righthead
        return dum.next

    def reverse(self,head):
        p=head
        q=p.next if p else None
        r=q.next if q else None
        if p:
            p.next=None
        while q:
            q.next=p
            p=q
            q=r
            r=r.next if r else None
        return p,head




