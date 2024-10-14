#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/8 00:26
# @Author  : sunaolin
# @File    : 147_4.py

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p=head
        dum=ListNode(0)
        while p:
            q=p.next
            r=dum
            while r.next and p.val>r.next.val:
                r=r.next
            p.next=r.next
            r.next=p
            p=q
        return dum.next