#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 21:35
# @Author  : sunaolin
# @File    : 445_1.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ll1 = []
        ll2 = []
        p = l1
        while p:
            ll1.append(p)
            p = p.next
        p = l2
        while p:
            ll2.append(p)
            p = p.next

        newhead = ListNode(0)

        c = 0

        for i in range(max(len(ll1), len(ll2))):
            if len(ll1) - 1 - i >= 0:
                v1 = ll1[len(ll1) - 1 - i].val
            else:
                v1 = 0
            if len(ll2) - 1 - i >= 0:
                v2 = ll2[len(ll2) - 1 - i].val
            else:
                v2 = 0
            print(v1, v2)
            tmp = ListNode((v1 + v2 + c) % 10)
            c = int((v1 + v2 + c) / 10)
            tmp.next = newhead.next
            newhead.next = tmp

        if c:
            tmp=ListNode(1)
            tmp.next=newhead.next
            newhead.next=tmp
        return newhead.next




