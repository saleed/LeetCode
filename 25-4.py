#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 14:31
# @Author  : sunaolin
# @File    : 25_3.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l=0
        dum=ListNode(0)
        dum.next=head
        p=dum
        start=dum
        while p.next:
            l+=1
            if l==k:
                print(p.next.val)
                q=p.next.next
                newstart=start.next
                self.reverse(start,q)
                start=newstart
                p=start
                l=0
            p=p.next
        return dum.next

        ##翻转pq之间的节点
    def reverse(self,p,q):
        s=p.next
        p.next=None

        t=s.next if s else None
        r=t.next if t else None
        s.next=q
        while t!=q:
            t.next=s
            s=t
            t=r
            r=r.next if r else None
        p.next=s







