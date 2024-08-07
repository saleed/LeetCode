#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 10:39
# @Author  : yiheng
# @File    : 19_8.py
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        l=0
        p=head
        while p:
            l+=1
            p=p.next
        id=l-n+1   ##倒数第i个节点，正数第l-i+1个节点
        dum=ListNode(0)
        dum.next=head

        i=1
        p=dum
        while i<id:
            p=p.next
            i+=1
        if p.next:
            q=p.next
            p.next=q.next
            q.next=None
        return dum.next

