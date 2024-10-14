#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/3 15:47
# @Author  : sunaolin
# @File    : 86_3.py

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        q1=ListNode(0)
        r1=ListNode(0)

        q=q1
        r=r1
        p=head
        while p:
            s=p.next
            p.next=None
            if p.val<x:
                q.next=p
                q=q.next
            else:
                r.next=p
                r=r.next
            p=s
        q.next=r1.next
        return q1.next


