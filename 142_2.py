#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 19:22
# @Author  : sunaolin
# @File    : 142_2.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = p.next if p else None
        while p != None and q != None:
            if p == q:
                break
            p = p.next
            q = q.next.next if q.next else None
        print(p.val, q.val)

        p = ListNode(0)
        p.next=head
        print(111)
        while p != q:
            p = p.next
            q = q.next
            print(p.val, q.val)
        return p
