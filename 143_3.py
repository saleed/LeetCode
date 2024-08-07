#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 19:41
# @Author  : sunaolin
# @File    : 143_3.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        nlist=[]
        p=head
        while p:
            nlist.append(p)
            q=p.next  ##系统检测到有环，就会在下面报错
            p.next=None
            p=q
        newhead=ListNode(0)
        print(nlist)

        r=newhead
        p=0
        q=len(nlist)-1
        while p<q:
            print(p,q)
            r.next=nlist[p]
            p+=1
            r=r.next
            r.next=nlist[q]
            r=r.next
            q-=1
            print(newhead)

        if p==q:
            r.next=nlist[p]
            nlist[p].next=None

        return newhead.next