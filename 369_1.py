#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 17:31
# @Author  : sunaolin
# @File    : 369——1.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ln=[]
        p=head
        while p:
            ln.append(p)
            p=p.next
        c=1
        for i in range(len(ln))[::-1]:
            newval=(ln[i].val+c)%10
            c=(ln[i].val+c)//10
            ln[i].val=newval
        if c>0:
            newhead=ListNode(c)
            newhead.next=head
            return newhead
        else:
            return head

