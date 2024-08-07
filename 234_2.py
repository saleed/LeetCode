#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 13:59
# @Author  : sunaolin
# @File    : 234_2.py

# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return head
        l=0
        p=head
        while p:
            l+=1
            p=p.next


        cnt=0
        p=head
        while cnt<l/2-1:
            cnt+=1
            p=p.next
        if l%2==0:
            p2=p.next
        else:
            p2=p.next.next
        p.next=None
        p=head
        q=head.next
        r=q.next if q else None
        p.next=None
        while q:
            q.next=p
            p=q
            q=r
            r=r.next if r else None
        p1=p
        while p1!=None and p2!=None:
            if p1.val==p2.val:
                p1=p1.next
                p2=p2.next
            else:
                return False
        return True








