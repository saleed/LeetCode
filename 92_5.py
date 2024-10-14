#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/4 12:33
# @Author  : sunaolin
# @File    : 92_5.py


###链表题一定要把链表该断掉的next指针提前断掉


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        dum=ListNode(0)
        dum.next=head
        p=dum
        n=1

        prel=None
        while n<left:
            p=p.next
            n+=1
        prel=p
        while n<right:
            p=p.next
            n+=1
        prer=p

        l=prel.next
        r=prer.next
        nxtr=r.next

        prel.next=None
        r.next=None

        head,tail=self.reverse(l)
        prel.next=head
        tail.next=nxtr
        return dum.next

    def reverse(self,head):
        p=head
        q=head.next if p else None
        r=q.next if q else None
        p.next=None
        while q:
            q.next=p
            p=q
            q=r
            r=r.next if r else None

        return p,head



