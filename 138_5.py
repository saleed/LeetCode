#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 22:17
# @Author  : sunaolin
# @File    : 138_5.py




class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        pmap={}

        p=head
        dum=ListNode(0)
        r=dum
        while p:
            r.next=ListNode(p.val)
            pmap[p]=r
            r=r.next
        p=head
        r=dum.next
        while p:
            if p.random!=None:
                r.random=pmap[p.random]
            else:
                r.random=None
            r=r.next
            p=p.next
        return dum.next
