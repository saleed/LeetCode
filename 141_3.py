#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 14:36
# @Author  : sunaolin
# @File    : 141——3.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p=head
        q=p.next if p else None

        while p!=None and q!=None :
            if p==q:
                return True
            p=p.next
            q=q.next.next if q.next else None
        return False
